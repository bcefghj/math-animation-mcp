# Docker 安装指南

Docker 是最简单的安装方式——不需要安装 Python、LaTeX、FFmpeg 等依赖。

## 前提条件

安装 Docker Desktop：
- **macOS**: https://docs.docker.com/desktop/install/mac-install/
- **Windows**: https://docs.docker.com/desktop/install/windows-install/
- **Linux**: https://docs.docker.com/engine/install/

## 一键启动

```bash
docker run -p 7860:7860 -v ./output:/app/animation_output math-animation-mcp
```

打开浏览器访问 http://localhost:7860 即可使用。

## 使用 docker-compose（推荐）

创建 `docker-compose.yml`：

```yaml
services:
  math-animation:
    image: math-animation-mcp:latest
    ports:
      - "7860:7860"
    volumes:
      - ./output:/app/animation_output
      - ./config:/app/config
    environment:
      - DEFAULT_STYLE=three_blue_one_brown
      - LANG=zh_CN.UTF-8
```

启动：

```bash
docker compose up -d
```

停止：

```bash
docker compose down
```

## 输出文件

渲染的视频保存在 `./output/` 目录（挂载到容器的 `/app/animation_output`）。

## 自定义配置

通过环境变量自定义：

```yaml
environment:
  - DEFAULT_STYLE=khan_academy     # 默认风格
  - DEFAULT_QUALITY=high           # 默认质量
  - OUTPUT_DIR=/app/animation_output
```
