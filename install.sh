#!/usr/bin/env bash
# Math Animation MCP - One-click installer for macOS and Linux
set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

info() { echo -e "${GREEN}[INFO]${NC} $1"; }
warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
error() { echo -e "${RED}[ERROR]${NC} $1"; exit 1; }

echo ""
echo "================================================="
echo "   Math Animation MCP - 数学动画 MCP 安装器"
echo "================================================="
echo ""

# Detect OS
OS="$(uname -s)"
case "$OS" in
    Darwin) PLATFORM="macos";;
    Linux)  PLATFORM="linux";;
    *)      error "Unsupported OS: $OS";;
esac
info "Detected platform: $PLATFORM"

# Check Python
if command -v python3 &>/dev/null; then
    PY_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
    info "Python $PY_VERSION found"
else
    error "Python 3 not found. Please install Python 3.11+ first."
fi

# Install system dependencies
if [ "$PLATFORM" = "macos" ]; then
    if ! command -v brew &>/dev/null; then
        warn "Homebrew not found. Installing..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi
    info "Installing system dependencies via Homebrew..."
    brew install cairo pango ffmpeg pkg-config 2>/dev/null || true
    info "System dependencies installed"

elif [ "$PLATFORM" = "linux" ]; then
    if command -v apt &>/dev/null; then
        info "Installing system dependencies via apt..."
        sudo apt update
        sudo apt install -y libcairo2-dev libpango1.0-dev ffmpeg texlive texlive-lang-chinese \
            fonts-noto-cjk pkg-config python3-pip
    elif command -v dnf &>/dev/null; then
        info "Installing system dependencies via dnf..."
        sudo dnf install -y cairo-devel pango-devel ffmpeg texlive texlive-ctex \
            google-noto-cjk-fonts pkg-config python3-pip
    elif command -v pacman &>/dev/null; then
        info "Installing system dependencies via pacman..."
        sudo pacman -S --noconfirm cairo pango ffmpeg texlive-core texlive-langchinese \
            noto-fonts-cjk pkg-config python-pip
    else
        warn "Unknown package manager. Please install manually: cairo, pango, ffmpeg, texlive, Chinese fonts"
    fi
fi

# Install math-animation-mcp
info "Installing math-animation-mcp..."
if command -v uv &>/dev/null; then
    uv pip install math-animation-mcp
else
    pip3 install math-animation-mcp
fi

# Verify installation
info "Verifying installation..."
python3 -c "import manim; print(f'  Manim version: {manim.__version__}')"
python3 -c "import math_animation_mcp; print(f'  math-animation-mcp version: {math_animation_mcp.__version__}')"

echo ""
echo "================================================="
echo "   安装完成！Installation complete!"
echo "================================================="
echo ""
echo "使用方式 Usage:"
echo ""
echo "  1. Web 界面 (推荐):"
echo "     math-animation-mcp --web"
echo "     然后打开浏览器 http://localhost:7860"
echo ""
echo "  2. MCP Server (Cursor):"
echo "     在 .cursor/mcp.json 中添加配置 (见 README)"
echo ""
echo "  3. Docker:"
echo "     docker run -p 7860:7860 math-animation-mcp"
echo ""
