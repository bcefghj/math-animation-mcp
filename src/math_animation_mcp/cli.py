"""CLI entry point for math-animation-mcp."""

from __future__ import annotations

import argparse
import sys


def main():
    parser = argparse.ArgumentParser(
        prog="math-animation-mcp",
        description="Math Animation MCP Server - Generate 3Blue1Brown-style teaching animations",
    )
    parser.add_argument(
        "--web", action="store_true",
        help="Start the Gradio web interface instead of MCP server",
    )
    parser.add_argument(
        "--port", type=int, default=7860,
        help="Port for web interface (default: 7860)",
    )
    parser.add_argument(
        "--output-dir", default="./animation_output",
        help="Output directory for rendered animations",
    )

    args = parser.parse_args()

    import os
    os.environ["OUTPUT_DIR"] = args.output_dir

    if args.web:
        from math_animation_mcp.web_server import launch
        launch(port=args.port)
    else:
        from math_animation_mcp.server import run
        run()


if __name__ == "__main__":
    main()
