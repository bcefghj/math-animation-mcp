# 🎬 Math Animation MCP

> **一键生成 3Blue1Brown 风格的数学教学动画**
>
> 支持文字描述 / LaTeX 公式 / PDF 试卷 / 图片截图 → 自动输出教学视频。
> 中文高考 / 中考知识点全覆盖，面向零基础用户设计。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Manim](https://img.shields.io/badge/Manim-0.18+-green.svg)](https://www.manim.community/)
[![MCP](https://img.shields.io/badge/MCP-Compatible-purple.svg)](https://modelcontextprotocol.io/)

---

## 目录

- [这是什么？](#这是什么)
- [能做什么？效果示例](#能做什么效果示例)
- [30 秒快速开始](#30-秒快速开始)
  - [方式 A：Docker（最简单，什么都不用装）](#方式-adocker最简单什么都不用装)
  - [方式 B：Cursor MCP（推荐程序员）](#方式-bcursor-mcp推荐程序员)
  - [方式 C：pip 安装](#方式-cpip-安装)
- [功能详解](#功能详解)
  - [支持的输入方式](#支持的输入方式)
  - [6 种视觉风格](#6-种视觉风格)
  - [5 级受众适配](#5-级受众适配)
  - [10+ 预置模板](#10-预置模板)
  - [21 个 MCP 工具](#21-个-mcp-工具)
- [安装指南（各平台详细步骤）](#安装指南各平台详细步骤)
- [使用教程（带截图）](#使用教程带截图)
- [项目结构说明](#项目结构说明)
- [常见问题 FAQ](#常见问题-faq)
- [开源协议](#开源协议)

---

## 这是什么？

这是一个 **AI + 数学动画** 工具，核心能力：

1. **你描述题目或概念** → AI 自动生成漂亮的动画视频
2. **上传 PDF 试卷或图片** → OCR 识别后自动讲解每道题
3. **对话式修改** → 「字再大一点」「换成黑板风格」「慢一些」
4. **零编程基础可用** → Web 界面点点就行，不需要会写代码

底层使用 [Manim Community Edition](https://www.manim.community/)（3Blue1Brown 同款动画引擎）+ [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) 实现 AI 对话控制。

---

## 能做什么？效果示例

### 示例 1：勾股定理可视化证明

**输入：** `帮我做一个勾股定理的证明动画，适合初中生看`

**输出效果：**
- 直角三角形逐步出现，三边分别标注 a、b、c
- 三个正方形从各边长出，面积用颜色填充
- 文字说明：`a² + b² = c²` 动态写出
- 最终公式高亮闪烁，配合步骤解说字幕

```
📁 animation_output/
  └── pythagorean_theorem_middle_school.mp4  (约 45 秒, 1080p)
```

---

### 示例 2：高考真题 PDF 讲解

**输入：** 上传 `2024高考数学全国卷.pdf`，然后说：`帮我讲解第 3 题`

**输出：**
- 题目文字出现在画面左边
- 解题步骤逐步展示在右边
- 关键计算步骤有动画演示
- 最终选项高亮标出正确答案

---

### 示例 3：函数图像变换

**输入：** `展示 y=sin(x) 通过平移、缩放、翻转变成各种形式的过程`

**输出：**
- 坐标系从中心展开
- 正弦曲线动态绘制
- 参数 A、ω、φ 分别变化，图像实时跟随变形
- 每个变换配文字说明

---

### 示例 4：LaTeX 公式讲解

**输入：** `\int_0^{\pi} \sin(x)\,dx = 2`

**输出：**
- 公式从左到右逐字写出
- 坐标系上 sin(x) 曲线绘制
- 0 到 π 的区域用颜色填充
- 标注面积 = 2，连线指向公式

---

## 30 秒快速开始

> 💡 **零基础推荐方式 A（Docker），5 分钟内看到效果。**

---

### 方式 A：Docker（最简单，什么都不用装）

前提：安装好 [Docker Desktop](https://www.docker.com/products/docker-desktop/)（官网下载，双击安装，免费）

```bash
# 第一步：拉取镜像（需要几分钟，只需做一次）
docker pull math-animation-mcp

# 第二步：启动
docker run -p 7860:7860 -v ./output:/app/animation_output math-animation-mcp

# 第三步：打开浏览器
# 访问 http://localhost:7860
```

或者用 docker-compose 一键启动（克隆本仓库后执行）：

```bash
git clone https://github.com/bcefghj/math-animation-mcp.git
cd math-animation-mcp
docker compose up -d
# 访问 http://localhost:7860
```

---

### 方式 B：Cursor MCP（推荐程序员）

> 需要已安装 [Cursor 编辑器](https://cursor.com/)（免费）

**第一步：** 在你的项目根目录创建文件 `.cursor/mcp.json`：

```json
{
  "mcpServers": {
    "math-animation": {
      "command": "uvx",
      "args": ["math-animation-mcp"],
      "env": {
        "OUTPUT_DIR": "./animation_output"
      }
    }
  }
}
```

**第二步：** 重启 Cursor，打开 AI 对话框（`Cmd+L` 或 `Ctrl+L`）

**第三步：** 直接说话：

```
帮我做一个勾股定理的证明动画

@高考真题.pdf 帮我把第 3 题做成讲解动画

把这段关于导数的文字做成教学动画，黑板风格，高中生受众

动画太快了，字再大一点，换成可汗学院风格
```

---

### 方式 C：pip 安装

> 需要 Python 3.11+。如果你没有 Python，[点这里下载](https://www.python.org/downloads/)

```bash
# 安装
pip install math-animation-mcp

# 启动 Web 界面
math-animation-mcp --web
# 访问 http://localhost:7860

# 或者直接渲染（命令行）
math-animation-mcp render --text "勾股定理证明" --style three_blue_one_brown --quality medium
```

---

## 功能详解

### 支持的输入方式

| 输入类型 | 说明 | 示例 |
|---------|------|------|
| **自然语言** | 直接描述你想要的动画 | `「帮我做一个勾股定理的证明动画」` |
| **LaTeX 公式** | 粘贴数学公式 | `` `\int_0^{\pi} \sin(x) dx = 2` `` |
| **PDF 文件** | 上传试卷或教材 PDF | 拖入 `高考2024.pdf` |
| **图片/截图** | 手机拍照或截图题目 | 上传 `题目.jpg` |
| **文章段落** | 粘贴教材中的段落文字 | 粘贴一段微积分讲解 |
| **修改指令** | 口语化调整已有动画 | `「字再大一点」「慢一些」「换颜色」` |

---

### 6 种视觉风格

| 风格名称 | 背景色 | 适合场景 | 预览 |
|---------|-------|---------|------|
| `three_blue_one_brown` | 深灰 `#1C1C1C` | 科普、大学教学（经典 3B1B 配色） | 深色背景 + 蓝/黄高亮 |
| `khan_academy` | 白色 `#FFFFFF` | 中小学教学（柔和明亮） | 白底 + 彩色线条 |
| `textbook` | 浅灰 `#F5F5F5` | 正式论文、教科书 | 极简风格 |
| `playful` | 暖黄 `#FFF8E1` | 小学、低龄学生 | 彩色活泼 |
| `dark_tech` | 纯黑 `#000000` | 大学、竞赛、CS | 霓虹配色 |
| `blackboard` | 深绿 `#2D5016` | 课堂模拟 | 粉笔白字 |

切换风格只需一句话：「换成黑板风格」或在代码中：

```python
result = render_animation(code, style="blackboard")
```

---

### 5 级受众适配

系统会根据受众级别自动调整**动画速度、字体大小、讲解详细程度**：

| 级别 | 受众 | 速度 | 字体 | 讲解 |
|-----|------|------|-----|------|
| L1 | 小学生 | 0.5× 慢速 | 最大 | 每步都有解释，大量停顿 |
| L2 | 初中生 | 0.7× | 大 | 详细解释 |
| L3 | 高中生 | 1.0× 正常 | 正常 | 适中 |
| L4 | 大学生 | 1.2× | 小 | 简洁 |
| L5 | 竞赛/研究 | 1.5× 快速 | 最小 | 最精简 |

设置方式：「以后默认受众是初中生」或：

```json
{
  "audience_level": 2,
  "style": "khan_academy"
}
```

---

### 10+ 预置模板

覆盖中高考核心知识点，开箱即用：

| 分类 | 模板名称 | 适用年级 |
|-----|---------|---------|
| 几何 | 勾股定理证明、圆的性质、相似三角形 | 初中 |
| 代数 | 一元二次方程、函数图像变换、因式分解 | 初中/高中 |
| 微积分 | 导数切线、定积分面积、极限 | 高中/大学 |
| 三角函数 | 单位圆、正弦余弦、和差化积 | 高中 |
| 统计概率 | 正态分布、频率直方图、排列组合 | 高中 |
| 物理 | 抛体运动、受力分析、电路图 | 高中 |
| 计算机 | 排序算法、二分查找、递归树 | 大学/竞赛 |

---

### 21 个 MCP 工具

<details>
<summary>点击展开完整工具列表</summary>

**渲染工具（3个）**
- `render_animation(code, quality, format, style)` — 渲染完整视频
- `preview_scene(code, style)` — 快速 480p 预览（速度快 10 倍）
- `render_gif(code, style)` — 导出 GIF 动图

**模板工具（3个）**
- `list_templates(category, difficulty)` — 浏览所有模板
- `get_template(template_id)` — 获取模板源代码
- `search_templates(keyword)` — 关键词搜索模板

**输入处理（5个）**
- `detect_input_type(content)` — 自动识别输入类型
- `parse_pdf(file_path)` — 解析 PDF，提取文字和公式
- `parse_image(file_path)` — OCR 图片，识别数学公式
- `fix_ocr_errors(text)` — 修复 OCR 常见错误
- `normalize_content(raw_text)` — 结构化提取内容

**自修复工具（3个）**
- `analyze_error(code, error_msg)` — 分析错误类型
- `fix_latex_error(code, error_msg)` — 自动修复 LaTeX 错误
- `fix_python_error(code, error_msg)` — 自动修复 Python/Manim API 错误

**个性化工具（4个）**
- `set_style(style_name)` — 切换视觉风格
- `set_preferences(preferences_json)` — 更新用户偏好
- `get_preferences()` — 读取当前设置
- `set_branding(watermark, logo_path, intro_text, outro_text)` — 设置品牌水印

**导出工具（3个）**
- `export_video(file_path, format, aspect_ratio)` — 格式/比例转换
- `add_subtitles(video_path, text)` — 烧录字幕
- `add_tts_narration(video_path, script, voice)` — 配音（即将推出）

</details>

---

## 安装指南（各平台详细步骤）

### macOS（苹果电脑）

**方法 1：一键安装脚本（最简单）**

打开「终端」（在 Spotlight 搜索 `终端`），粘贴以下命令：

```bash
curl -fsSL https://raw.githubusercontent.com/bcefghj/math-animation-mcp/main/install.sh | bash
```

等待安装完成（约 5-10 分钟），然后：

```bash
math-animation-mcp --web
```

**方法 2：手动安装（遇到问题时用这个）**

```bash
# 第一步：安装 Homebrew（如果还没有）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 第二步：安装系统依赖
brew install cairo pango ffmpeg

# 第三步：安装字体（中文支持）
brew install --cask font-noto-sans-cjk

# 第四步：安装 Python 包
pip3 install math-animation-mcp

# 第五步：启动
math-animation-mcp --web
```

---

### Windows（10 / 11）

**方法 1：一键安装脚本**

以管理员身份打开「PowerShell」（开始菜单搜索 `PowerShell`，右键「以管理员身份运行」）：

```powershell
irm https://raw.githubusercontent.com/bcefghj/math-animation-mcp/main/install.ps1 | iex
```

**方法 2：手动安装**

```powershell
# 第一步：安装 Chocolatey 包管理器（如果还没有）
Set-ExecutionPolicy Bypass -Scope Process -Force
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# 第二步：安装依赖
choco install manimce ffmpeg -y

# 第三步：安装 Python 包
pip install math-animation-mcp

# 第四步：启动
math-animation-mcp --web
```

> ⚠️ Windows 用户：如果遇到 LaTeX 相关错误，需要额外安装 [MiKTeX](https://miktex.org/download)（免费）

---

### Linux（Ubuntu / Debian）

```bash
# 第一步：安装系统依赖
sudo apt update
sudo apt install -y libcairo2-dev libpango1.0-dev ffmpeg texlive-full fonts-noto-cjk

# 第二步：安装 Python 包
pip install math-animation-mcp

# 第三步：启动
math-animation-mcp --web
```

---

### Docker（任何平台，推荐小白使用）

只需安装好 [Docker Desktop](https://www.docker.com/products/docker-desktop/)，然后：

```bash
# 克隆仓库
git clone https://github.com/bcefghj/math-animation-mcp.git
cd math-animation-mcp

# 一键启动（后台运行）
docker compose up -d

# 访问 Web 界面
# 打开浏览器访问 http://localhost:7860

# 停止服务
docker compose down
```

---

## 使用教程（带截图）

### 教程 1：用 Web 界面生成第一个动画

1. 启动服务后，打开浏览器访问 `http://localhost:7860`
2. 在「输入」框中输入：`勾股定理的几何证明，适合初中生看`
3. 在「风格」下拉菜单选择 `three_blue_one_brown`
4. 在「质量」中选择 `medium`（中等质量，速度较快）
5. 点击「生成动画」按钮
6. 等待约 30-60 秒，视频出现在右侧预览区
7. 点击「下载」保存到本地

```
📌 提示：第一次渲染会慢一些（需要加载 LaTeX 等组件），后续会快很多。
```

---

### 教程 2：在 Cursor 中对话生成动画

1. 安装好 MCP 配置（见[方式 B](#方式-bcursor-mcp推荐程序员)）
2. 打开 Cursor，按 `Cmd+L`（Mac）或 `Ctrl+L`（Windows）打开 AI 对话
3. 输入：

```
帮我做一个展示函数 y=x² 图像的动画，用暗色科技风格，大学生受众
```

4. AI 会自动：
   - 检测输入类型（函数可视化）
   - 查找最接近的模板
   - 生成 Manim 代码
   - 渲染视频（会显示进度）
5. 渲染完成后，视频保存在 `./animation_output/` 文件夹
6. 如果想修改，直接说：

```
把坐标轴颜色改成蓝色，加上 x=-2 到 x=2 的范围标注
```

---

### 教程 3：上传 PDF 试卷自动讲解

1. 准备一个 PDF 文件（高考数学试卷、教材章节等）
2. 在 Cursor AI 对话中输入：

```
@2024高考数学.pdf 帮我讲解第 5 题，可汗学院风格，高中生受众
```

3. 系统会：
   - 解析 PDF 文件
   - 识别第 5 题的题目和解题过程
   - 生成逐步讲解动画

> 💡 **提示**：PDF 中的数学公式如果是扫描版（图片格式），系统会自动 OCR 识别，但准确率约 85-95%，识别后可以对话修正。

---

### 教程 4：对话式修改动画

动画生成后，你可以用自然语言调整：

| 你说的话 | 效果 |
|---------|------|
| `字再大一点` | 所有文字字号 +20% |
| `慢一些` | 动画速度 ×0.7 |
| `换成黑板风格` | 切换为 blackboard 风格 |
| `加个水印，写上"张老师课堂"` | 右下角添加水印 |
| `导出 GIF` | 转换为 GIF 格式 |
| `竖屏版，适合手机观看` | 导出 9:16 比例 |

---

## 项目结构说明

> 这部分面向想深入了解或二次开发的用户

```
math-animation-mcp/
│
├── 📄 pyproject.toml          # Python 包配置（版本、依赖等）
├── 🐳 Dockerfile              # Docker 镜像配置
├── 🐳 docker-compose.yml      # 一键启动配置
├── 🔧 install.sh              # macOS/Linux 一键安装脚本
├── 🔧 install.ps1             # Windows 一键安装脚本
│
├── 📁 src/math_animation_mcp/
│   ├── server.py              # 核心：MCP Server，注册 21 个工具
│   ├── web_server.py          # Web 界面（基于 Gradio）
│   ├── cli.py                 # 命令行入口
│   │
│   ├── 📁 tools/
│   │   ├── render_tools.py    # 渲染：生成视频/GIF
│   │   ├── template_tools.py  # 模板：浏览/搜索/获取
│   │   ├── input_tools.py     # 输入：PDF/图片/文字处理
│   │   ├── repair_tools.py    # 自修复：错误分析和自动修复
│   │   ├── personalization_tools.py  # 个性化：风格/偏好
│   │   └── export_tools.py    # 导出：格式转换/字幕/配音
│   │
│   ├── 📁 templates/          # 10+ 预置动画模板
│   │   ├── geometry/          # 几何（勾股定理、圆等）
│   │   ├── algebra/           # 代数（方程、函数等）
│   │   ├── calculus/          # 微积分（导数、积分等）
│   │   ├── trigonometry/      # 三角函数
│   │   ├── statistics/        # 统计概率
│   │   ├── physics/           # 物理
│   │   └── cs/                # 计算机科学
│   │
│   ├── 📁 styles/
│   │   └── presets.py         # 6 种视觉风格配置
│   │
│   ├── 📁 config/             # 用户偏好配置文件
│   └── 📁 utils/              # 工具函数（沙箱、中文支持等）
│
├── 📁 docs/                   # 详细文档
│   ├── getting-started/       # 入门教程
│   ├── tutorials/             # 进阶教程
│   └── faq/                   # 常见问题
│
└── 📁 animation_output/       # 生成的动画视频（自动创建）
```

---

## 常见问题 FAQ

**Q: 我完全不会编程，能用吗？**

完全可以！有三种零编程方式：
- Docker + Web 界面：浏览器里点点就行
- Cursor MCP：在 Cursor 里说话就行
- pip + Web 界面：一行命令启动，然后浏览器操作

---

**Q: 渲染一个动画需要多长时间？**

| 质量 | 时长（30 秒动画） | 适合场景 |
|-----|-----------------|---------|
| `low` (480p) | 约 10-20 秒 | 快速预览 |
| `medium` (720p) | 约 30-60 秒 | 日常使用 |
| `high` (1080p) | 约 2-5 分钟 | 最终输出 |
| `ultra` (4K) | 约 10-30 分钟 | 专业发布 |

---

**Q: 中文显示乱码怎么办？**

确保安装了中文字体：

```bash
# macOS
brew install --cask font-noto-sans-cjk

# Ubuntu
sudo apt install fonts-noto-cjk

# Windows：下载 Noto Sans CJK 字体包安装
# https://www.google.com/get/noto/
```

Docker 版已预装所有字体，不存在此问题。

---

**Q: 渲染失败了怎么办？**

系统内置自修复机制：
1. 失败后自动分析错误类型（LaTeX 错误 / Python 错误 / 资源不足）
2. 自动修复并重试，最多尝试 5 次
3. 连续失败会自动降级到最接近的预置模板
4. 如果你看到"已降级到模板"的提示，说明自动修复已处理，动画仍会正常生成

---

**Q: 没有 LaTeX 环境怎么办？**

- **Docker 版**：已包含完整 LaTeX，无需操心
- **本地安装版**：
  - macOS：`brew install --cask mactex`（约 4GB）
  - Windows：安装 [MiKTeX](https://miktex.org/download)（推荐）或 [TeX Live](https://www.tug.org/texlive/)
  - Ubuntu：`sudo apt install texlive-full`
- **临时方案**：在代码中用 `Text()` 代替 `MathTex()`（纯文字，无需 LaTeX）

---

**Q: 可以商用吗？**

本项目基于 [MIT 协议](LICENSE)，可以免费用于个人和商业用途，唯一要求是保留原始版权声明。

---

**Q: 怎么给动画加自己的 Logo 或水印？**

```python
# 通过 set_branding 工具设置
set_branding(
    watermark="张老师课堂",        # 右下角文字水印
    logo_path="./my_logo.png",    # Logo 图片（可选）
    intro_text="张老师数学课",     # 片头文字
    outro_text="关注我，每天一题"  # 片尾文字
)
```

或者在 Cursor 中直接说：「加个水印，写上"张老师课堂"」

---

**Q: 可以导出竖屏版本吗（适合短视频）？**

```python
export_video(
    file_path="output.mp4",
    format="mp4",
    aspect_ratio="9:16"  # 抖音/视频号/Reels 格式
)
```

或说：「导出竖屏版，9:16 比例」

---

## 开源协议

本项目基于 [MIT License](LICENSE) 开源，欢迎 Star、Fork、提 Issue 和 PR！

---

## 相关链接

- [Manim Community 官网](https://www.manim.community/) — 底层动画引擎
- [Model Context Protocol](https://modelcontextprotocol.io/) — MCP 协议文档
- [Cursor 编辑器](https://cursor.com/) — 推荐的 AI 编程工具
- [3Blue1Brown](https://www.youtube.com/@3blue1brown) — 灵感来源

---

*Made with ❤️ for math education*
