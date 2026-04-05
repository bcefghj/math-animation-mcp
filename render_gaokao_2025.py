"""Render 2025 Gaokao real exam problems: 3 long animations."""
import os, sys, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
from math_animation_mcp.utils.sandbox import render_manim_code

OUTPUT = os.path.join(os.path.dirname(__file__), "animation_output", "gaokao_2025")
os.makedirs(OUTPUT, exist_ok=True)

cases = {
    "17_solid_geometry": "gaokao_2025_17_solid.py",
    "18_ellipse_conic": "gaokao_2025_18_ellipse.py",
    "19_derivative_trig": "gaokao_2025_19_derivative.py",
}

for name, filename in cases.items():
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path, "r") as f:
        code = f.read()

    # Extract the class body between triple quotes
    # The files have the code inside triple-quoted strings as module-level docstrings + actual class
    # Actually, these files are full Python scripts. We just run them directly.
    print(f"\n[Rendering] {name} from {filename} ...")
    t0 = time.time()
    result = render_manim_code(code, quality="low", fmt="mp4", output_dir=OUTPUT, timeout=300)
    elapsed = time.time() - t0

    if result.success:
        size_kb = os.path.getsize(result.file_path) / 1024
        print(f"  OK ({elapsed:.1f}s, {size_kb:.0f}KB) -> {os.path.basename(result.file_path)}")
    else:
        print(f"  FAIL ({elapsed:.1f}s)")
        print(f"  Error: {result.error_msg[-500:]}")
