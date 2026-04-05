"""Self-healing MCP tools: error analysis, LaTeX fixing, Python fixing."""

from __future__ import annotations

import re


def analyze_error(code: str, error_msg: str) -> dict:
    """Analyze a Manim render error and categorize it.

    Args:
        code: The Manim code that failed.
        error_msg: The error message / traceback.

    Returns:
        Dict with error_type, description, suggested_fix.
    """
    error_lower = error_msg.lower()

    if any(kw in error_lower for kw in ["latex", "tex", "dvi", "compilation", "undefined control sequence"]):
        fix_hint = _analyze_latex_error(error_msg)
        return {
            "error_type": "latex",
            "description": "LaTeX compilation error",
            "details": error_msg[-500:],
            "suggested_fix": fix_hint,
        }

    if any(kw in error_lower for kw in ["syntaxerror", "syntax error", "indentationerror"]):
        return {
            "error_type": "python_syntax",
            "description": "Python syntax error",
            "details": error_msg[-500:],
            "suggested_fix": "Check for typos, unmatched brackets, incorrect indentation.",
        }

    if any(kw in error_lower for kw in ["importerror", "modulenotfounderror", "no module named"]):
        module = re.search(r"No module named '([^']+)'", error_msg)
        return {
            "error_type": "import_error",
            "description": f"Missing module: {module.group(1) if module else 'unknown'}",
            "details": error_msg[-500:],
            "suggested_fix": f"Add the correct import or install the module.",
        }

    if any(kw in error_lower for kw in ["attributeerror", "has no attribute"]):
        return {
            "error_type": "api_error",
            "description": "Manim API usage error (wrong attribute/method)",
            "details": error_msg[-500:],
            "suggested_fix": "Check ManimCE docs for correct API names. API may have changed between versions.",
        }

    if any(kw in error_lower for kw in ["typeerror", "valueerror"]):
        return {
            "error_type": "type_error",
            "description": "Type or value error in arguments",
            "details": error_msg[-500:],
            "suggested_fix": "Check argument types and values passed to Manim objects/methods.",
        }

    if any(kw in error_lower for kw in ["timeout", "timed out"]):
        return {
            "error_type": "timeout",
            "description": "Render timed out - scene may be too complex",
            "details": error_msg[-500:],
            "suggested_fix": "Simplify the scene: reduce object count, shorten animations, lower quality.",
        }

    return {
        "error_type": "unknown",
        "description": "Unrecognized error",
        "details": error_msg[-500:],
        "suggested_fix": "Review the full traceback and fix the root cause.",
    }


def _analyze_latex_error(error_msg: str) -> str:
    if "undefined control sequence" in error_msg.lower():
        cmd = re.search(r"Undefined control sequence.*?(\\[a-zA-Z]+)", error_msg)
        if cmd:
            return f"Undefined LaTeX command: {cmd.group(1)}. Add the required package or fix the command name."
        return "An undefined LaTeX command was used. Check command spelling and required packages."

    if "missing $ inserted" in error_msg.lower():
        return "Math mode delimiter issue. Ensure math expressions are wrapped in $ or use MathTex instead of Tex."

    if "file ended" in error_msg.lower() or "unexpected end" in error_msg.lower():
        return "Unmatched braces in LaTeX. Check that all { have matching }."

    return "LaTeX compilation failed. Check formula syntax, escape backslashes properly in Python strings."


def fix_latex_error(code: str, error_msg: str) -> dict:
    """Attempt to auto-fix common LaTeX errors in Manim code.

    Args:
        code: The failing Manim code.
        error_msg: The error message.

    Returns:
        Dict with fixed_code and fixes_applied.
    """
    fixes: list[str] = []
    fixed = code

    # Double-backslash fix: raw strings often needed
    if "undefined control sequence" in error_msg.lower():
        # Ensure Tex/MathTex strings use raw strings
        def _fix_tex_strings(match: re.Match) -> str:
            prefix = match.group(1)
            quote = match.group(2)
            content = match.group(3)
            if not content.startswith("r"):
                return f'{prefix}r{quote}{content}{quote}'
            return match.group(0)

        pattern = r'((?:Tex|MathTex)\s*\(\s*)(["\'"])(.*?)\2'
        new_fixed = re.sub(pattern, _fix_tex_strings, fixed)
        if new_fixed != fixed:
            fixes.append("Added raw string prefix to Tex/MathTex arguments")
            fixed = new_fixed

    # Missing amsmath for common commands
    if any(cmd in error_msg for cmd in ["\\text", "\\operatorname", "\\mathrm"]):
        if "amsmath" not in fixed:
            fixed = fixed.replace(
                'from manim import *',
                'from manim import *\n# Ensure amsmath is available for LaTeX',
            )
            fixes.append("Note: amsmath may need to be added to tex template")

    # Unmatched braces
    open_count = fixed.count('{')
    close_count = fixed.count('}')
    if open_count > close_count:
        fixes.append(f"Warning: {open_count - close_count} unmatched opening braces detected")
    elif close_count > open_count:
        fixes.append(f"Warning: {close_count - open_count} unmatched closing braces detected")

    return {"fixed_code": fixed, "fixes_applied": fixes, "original_error": error_msg[:200]}


def fix_python_error(code: str, error_msg: str) -> dict:
    """Attempt to auto-fix common Python/Manim errors.

    Args:
        code: The failing Manim code.
        error_msg: The error message.

    Returns:
        Dict with fixed_code and fixes_applied.
    """
    fixes: list[str] = []
    fixed = code

    if "from manim import" not in fixed and "import manim" not in fixed:
        fixed = "from manim import *\n\n" + fixed
        fixes.append("Added 'from manim import *'")

    # Common API renames in recent ManimCE versions
    api_renames = [
        ("ShowCreation", "Create", "ShowCreation was renamed to Create"),
        ("FadeInFromDown", "FadeIn", "FadeInFromDown → FadeIn (with shift parameter)"),
        ("TextMobject", "Text", "TextMobject → Text"),
        ("TexMobject", "Tex", "TexMobject → Tex"),
    ]
    for old, new, desc in api_renames:
        if old in fixed and old in error_msg:
            fixed = fixed.replace(old, new)
            fixes.append(desc)

    # Scene class check
    if "class " not in fixed:
        fixes.append("Warning: No class definition found. Manim requires a Scene subclass.")

    if "def construct" not in fixed:
        fixes.append("Warning: No construct method found. Scene subclass needs def construct(self).")

    return {"fixed_code": fixed, "fixes_applied": fixes, "original_error": error_msg[:200]}
