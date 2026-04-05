"""Input processing MCP tools: detect type, parse PDF/image, fix OCR, normalize."""

from __future__ import annotations

import os
import re
from typing import Any


def detect_input_type(content: str) -> dict:
    """Auto-detect input type from content.

    Args:
        content: Raw text input from user.

    Returns:
        Dict with type, content_format, math_topic, confidence.
    """
    content_stripped = content.strip()

    has_latex = bool(re.search(r'\\(frac|int|sum|prod|sqrt|begin|end|alpha|beta|gamma|theta|pi|infty|lim|sin|cos|tan|log|ln)', content_stripped))
    has_chinese = any('\u4e00' <= ch <= '\u9fff' for ch in content_stripped)
    has_math_symbols = bool(re.search(r'[∫∑∏√∞±≤≥≠≈∈∉⊂⊃∪∩]', content_stripped))

    modification_keywords = ["修改", "改", "换", "大一点", "小一点", "快一点", "慢一点", "颜色", "风格", "字号"]
    is_modification = any(kw in content_stripped for kw in modification_keywords)

    if is_modification:
        return {"type": "modification", "content_format": "plain_text", "language": "zh" if has_chinese else "en", "confidence": 0.85}

    if has_latex and content_stripped.count('\\') > 2:
        return {"type": "latex_formula", "content_format": "latex", "language": "mixed" if has_chinese else "en", "confidence": 0.9}

    question_markers = ["求", "证明", "解", "计算", "已知", "若", "设", "则", "选择", "填空", "=", "?", "？"]
    is_math_problem = any(m in content_stripped for m in question_markers) or has_math_symbols

    if is_math_problem:
        topic = _detect_math_topic(content_stripped)
        return {"type": "math_problem", "content_format": "mixed" if has_latex else "plain_text",
                "math_topic": topic, "language": "zh" if has_chinese else "en", "confidence": 0.8}

    animation_keywords = ["动画", "可视化", "演示", "展示", "animate", "visualize", "show", "demonstrate"]
    is_animation_request = any(kw in content_stripped.lower() for kw in animation_keywords)
    if is_animation_request:
        return {"type": "animation_request", "content_format": "plain_text", "language": "zh" if has_chinese else "en", "confidence": 0.8}

    if len(content_stripped) > 200:
        return {"type": "article", "content_format": "plain_text", "language": "zh" if has_chinese else "en", "confidence": 0.6}

    return {"type": "concept_description", "content_format": "mixed" if has_latex else "plain_text",
            "language": "zh" if has_chinese else "en", "confidence": 0.5}


def _detect_math_topic(text: str) -> str:
    topic_keywords = {
        "geometry": ["三角形", "圆", "平行", "垂直", "角", "面积", "体积", "几何", "勾股", "triangle", "circle", "angle"],
        "algebra": ["方程", "函数", "多项式", "因式", "不等式", "数列", "equation", "function", "polynomial"],
        "calculus": ["导数", "积分", "极限", "微分", "连续", "derivative", "integral", "limit"],
        "trigonometry": ["sin", "cos", "tan", "正弦", "余弦", "正切", "三角函数", "弧度"],
        "statistics": ["概率", "期望", "方差", "正态", "分布", "随机", "probability", "distribution"],
        "linear_algebra": ["矩阵", "向量", "特征值", "行列式", "线性", "matrix", "vector", "eigenvalue"],
    }
    for topic, keywords in topic_keywords.items():
        if any(kw in text.lower() for kw in keywords):
            return topic
    return "general"


def parse_pdf(file_path: str, page_range: str | None = None) -> dict:
    """Extract text and formulas from a PDF file.

    Args:
        file_path: Path to the PDF file.
        page_range: Optional, e.g. "1-3" or "5".

    Returns:
        Dict with extracted text, formulas, and metadata.
    """
    if not os.path.exists(file_path):
        return {"success": False, "error": f"File not found: {file_path}"}

    try:
        import pix2text as p2t
        p = p2t.Pix2Text.from_config()
        result = p.recognize_pdf(file_path)
        text = result.to_markdown() if hasattr(result, 'to_markdown') else str(result)
        return {"success": True, "text": text, "source": "pix2text"}
    except ImportError:
        pass

    try:
        import subprocess
        result = subprocess.run(
            ["python", "-c", f"import fitz; doc = fitz.open('{file_path}'); print('\\n'.join(page.get_text() for page in doc))"],
            capture_output=True, text=True, timeout=30,
        )
        if result.returncode == 0:
            return {"success": True, "text": result.stdout, "source": "pymupdf"}
    except Exception:
        pass

    return {
        "success": False,
        "error": "No PDF parser available. Install pix2text: pip install pix2text",
        "hint": "Alternatively, paste the text content directly.",
    }


def parse_image(file_path: str) -> dict:
    """OCR an image to extract text and math formulas.

    Args:
        file_path: Path to the image file.

    Returns:
        Dict with extracted text and formulas.
    """
    if not os.path.exists(file_path):
        return {"success": False, "error": f"File not found: {file_path}"}

    try:
        import pix2text as p2t
        p = p2t.Pix2Text.from_config()
        result = p.recognize(file_path)
        text = result.to_markdown() if hasattr(result, 'to_markdown') else str(result)
        return {"success": True, "text": text, "source": "pix2text"}
    except ImportError:
        pass

    return {
        "success": False,
        "error": "No OCR engine available. Install pix2text: pip install pix2text",
        "hint": "Alternatively, type the content manually.",
    }


def fix_ocr_errors(text: str) -> dict:
    """Suggest fixes for common OCR errors in math text.

    This performs rule-based fixes. For LLM-powered fixing, the AI agent
    should analyze the text in its own context.

    Args:
        text: OCR output that may contain errors.

    Returns:
        Dict with cleaned text and list of fixes applied.
    """
    fixes: list[str] = []
    result = text

    replacements = [
        (r'(?<!\w)l(?=\d)', '1', 'l→1 (digit context)'),
        (r'(?<!\w)O(?=\d)', '0', 'O→0 (digit context)'),
        (r'\\frac\s*{', r'\\frac{', 'fix frac spacing'),
        (r'\\int\s*_', r'\\int_', 'fix integral spacing'),
        (r'(?<=\d)\s*x\s*(?=\d)', '×', 'x→× between digits'),
    ]

    for pattern, replacement, desc in replacements:
        new_result = re.sub(pattern, replacement, result)
        if new_result != result:
            fixes.append(desc)
            result = new_result

    return {"success": True, "original": text, "cleaned": result, "fixes_applied": fixes}


def normalize_content(raw_text: str) -> dict:
    """Normalize mixed content into a structured format.

    Args:
        raw_text: Raw text possibly containing LaTeX, Chinese, formulas.

    Returns:
        Structured dict with type, formulas, text_segments, language.
    """
    detected = detect_input_type(raw_text)

    formulas: list[str] = []
    inline = re.findall(r'\$([^$]+)\$', raw_text)
    display = re.findall(r'\$\$([^$]+)\$\$', raw_text)
    latex_cmds = re.findall(r'\\[a-zA-Z]+(?:\{[^}]*\})*', raw_text)
    formulas = display + inline + latex_cmds

    text_clean = re.sub(r'\$\$[^$]+\$\$', '', raw_text)
    text_clean = re.sub(r'\$[^$]+\$', '', text_clean)
    segments = [s.strip() for s in text_clean.split('\n') if s.strip()]

    return {
        "type": detected["type"],
        "math_topic": detected.get("math_topic", "general"),
        "formulas": list(set(formulas)),
        "text_segments": segments,
        "language": detected["language"],
        "raw": raw_text,
    }
