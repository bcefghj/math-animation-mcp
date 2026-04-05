# Math Animation MCP - One-click installer for Windows
# Run: irm https://raw.githubusercontent.com/your-name/math-animation-mcp/main/install.ps1 | iex

Write-Host ""
Write-Host "=================================================" -ForegroundColor Cyan
Write-Host "   Math Animation MCP - 数学动画 MCP 安装器" -ForegroundColor Cyan
Write-Host "=================================================" -ForegroundColor Cyan
Write-Host ""

# Check Chocolatey
if (-not (Get-Command choco -ErrorAction SilentlyContinue)) {
    Write-Host "[INFO] Installing Chocolatey..." -ForegroundColor Green
    Set-ExecutionPolicy Bypass -Scope Process -Force
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
    Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
}

# Install dependencies
Write-Host "[INFO] Installing system dependencies..." -ForegroundColor Green
choco install -y python ffmpeg manimce 2>$null

# Install math-animation-mcp
Write-Host "[INFO] Installing math-animation-mcp..." -ForegroundColor Green
pip install math-animation-mcp

# Verify
Write-Host "[INFO] Verifying installation..." -ForegroundColor Green
python -c "import manim; print(f'  Manim: {manim.__version__}')"
python -c "import math_animation_mcp; print(f'  math-animation-mcp: {math_animation_mcp.__version__}')"

Write-Host ""
Write-Host "=================================================" -ForegroundColor Cyan
Write-Host "   安装完成！Installation complete!" -ForegroundColor Cyan
Write-Host "=================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "使用方式:"
Write-Host "  1. Web: math-animation-mcp --web"
Write-Host "  2. MCP: 配置 .cursor/mcp.json"
Write-Host "  3. Docker: docker run -p 7860:7860 math-animation-mcp"
Write-Host ""
