# 常见问题与错误

## LaTeX 编译失败

**症状**: `LaTeX compilation error` 或 `Undefined control sequence`

**解决方案**:
1. 确保安装了完整 LaTeX（`texlive-full` 或通过 Docker）
2. 在 Python 字符串中使用双反斜杠：`r"\frac{1}{2}"` 或 `"\\frac{1}{2}"`
3. 使用 `MathTex` 代替 `Tex` 来写数学公式

## 中文显示问题

**症状**: 中文字符显示为方块或乱码

**解决方案**:
1. 使用 `Text("中文", font="STHeiti")` 而不是 `Tex`
2. 安装中文字体：`apt install fonts-noto-cjk`
3. Docker 镜像已预装中文字体

## 渲染超时

**症状**: `Render timed out after 120s`

**解决方案**:
1. 简化场景（减少对象数量和动画步骤）
2. 降低质量：`quality="low"`
3. 拆分为多个短场景

## FFmpeg 未找到

**症状**: `ffmpeg not found`

**解决方案**:
- macOS: `brew install ffmpeg`
- Ubuntu: `sudo apt install ffmpeg`
- Windows: `choco install ffmpeg`
- Docker: 已预装

## 模块找不到

**症状**: `ModuleNotFoundError: No module named 'manim'`

**解决方案**:
```bash
pip install manim
# 或
pip install math-animation-mcp
```

## MCP Server 连接失败

**症状**: Cursor 中工具不可用

**解决方案**:
1. 检查 `.cursor/mcp.json` 配置是否正确
2. 确保 `uvx` 或 `python` 可执行
3. 重启 Cursor
