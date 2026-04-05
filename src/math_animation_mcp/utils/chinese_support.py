"""Chinese font and ctex LaTeX configuration helpers."""

from __future__ import annotations

CTEX_PREAMBLE = r"""
\usepackage[UTF8]{ctex}
\setCJKmainfont{STSong}
\setCJKsansfont{STHeiti}
\setCJKmonofont{STFangsong}
"""

MANIM_CHINESE_TEX_TEMPLATE = r"""\documentclass[preview]{standalone}
\usepackage[UTF8]{ctex}
\usepackage{amsmath}
\usepackage{amssymb}
\begin{document}
YourCodeHere
\end{document}
"""


def get_chinese_tex_template_code() -> str:
    """Return a Manim TexTemplate snippet for Chinese support."""
    return '''
from manim import TexTemplate

chinese_tex_template = TexTemplate()
chinese_tex_template.add_to_preamble(r"\\usepackage[UTF8]{ctex}")
'''


def inject_chinese_support(code: str) -> str:
    """If code uses Chinese characters but has no ctex setup, inject it."""
    has_chinese = any('\u4e00' <= ch <= '\u9fff' for ch in code)
    if not has_chinese:
        return code
    if "ctex" in code:
        return code

    injection = (
        'from manim import TexTemplate\n'
        '_zh_template = TexTemplate()\n'
        '_zh_template.add_to_preamble(r"\\\\usepackage[UTF8]{ctex}")\n'
    )

    lines = code.split('\n')
    insert_idx = 0
    for i, line in enumerate(lines):
        if line.startswith('from manim') or line.startswith('import manim'):
            insert_idx = i + 1
    lines.insert(insert_idx, injection)
    return '\n'.join(lines)
