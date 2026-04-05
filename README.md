# 🎬 Math Animation MCP

> **一句话描述你想要的动画，AI 自动生成 3Blue1Brown 风格教学视频**
>
> 支持：文字描述 / LaTeX 公式 / PDF 试卷 / 图片截图 → 自动输出教学 MP4  
> 覆盖：高考/中考数学、物理、计算机科学，零编程基础可用

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://python.org)
[![Manim](https://img.shields.io/badge/powered%20by-Manim-brightgreen.svg)](https://www.manim.community/)
[![MCP](https://img.shields.io/badge/MCP-compatible-orange.svg)](https://modelcontextprotocol.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📺 效果展示

下面是本项目已渲染的真实案例（全部代码见 [`examples/`](examples/) 目录）：

### 🏆 2025 高考真题讲解（3 道大题）

| 题目 | 时长 | 内容亮点 |
|------|------|----------|
| [第17题 立体几何](examples/gaokao_2025/gaokao_2025_17_solid.py) | 1分13秒 | 四棱锥3D建模 + 360°旋转 + 球面可视化 + 二面角计算 |
| [第18题 圆锥曲线](examples/gaokao_2025/gaokao_2025_18_ellipse.py) | 1分32秒 | 椭圆逐步求解 + 动点轨迹动画 + |PM|最大值演示 |
| [第19题 导数压轴](examples/gaokao_2025/gaokao_2025_19_derivative.py) | 2分05秒 | f(x)=5cosx−cos5x 全解 + 和差化积可视化 + φ 扫描动画 |

### 📚 基础数学 15 个案例

| 案例 | 时长 | 知识点 |
|------|------|--------|
| 欧拉公式 | ~20s | $e^{i\pi}+1=0$，复平面旋转动画 |
| 配方法 | ~15s | 逐步配方 + 抛物线图像 |
| 三角函数变换 | ~15s | A/ω/φ 逐步变化对比 |
| 向量加法 | ~12s | 平行四边形法则 |
| ε-δ 极限定义 | ~15s | 可视化 ε 带和 δ 带 |
| 矩阵乘法 | ~15s | 逐元素展开 |
| 泰勒展开 | ~18s | 7 阶逼近 sin(x) |
| 贝叶斯定理 | ~20s | 韦恩图 + 医学检测案例 |
| 斐波那契/黄金比例 | ~18s | 比值趋近 φ 的折线图 |
| 复数平面 | ~15s | 复数运算几何意义 |
| 杨辉三角 | ~12s | 逐行生成 + 二项式定理 |
| 排序算法 | ~14s | 时间复杂度对比表 |
| 微积分基本定理 | ~20s | 面积可视化 |
| 简谐运动 | ~18s | 弹簧动画 + 实时波形描绘 |
| 3D 空间平面 | ~35s | 三维旋转 + 法向量 |

### 🔬 进阶长案例 12 个

| 案例 | 时长 | 知识点 |
|------|------|--------|
| 高考导数压轴 | 45s | f(x)=x−1−a·ln(x)，单调性讨论+不等式证明 |
| 3D 立体几何 | 30s | 正方体截面 + 二面角计算 |
| 高考含参函数 | 42s | f(x)=eˣ−ax−1，含参讨论 + 极值 |
| 高考递推数列 | 40s | 取倒数化等差 + 前 8 项验证 |
| 抛体运动 | 32s | 轨迹 + 实时速度矢量 + 三角度对比 |
| 电场力与电势 | 32s | 电场线 + 等势面 + 电偶极子 |
| 椭圆焦点性质 | 30s | 动点绕行，实时验证 |PF₁|+|PF₂|=2a |
| 弹簧能量守恒 | 32s | Ek/Ep 时间曲线 + 相空间椭圆 |
| 直线与圆 | 37s | 相交/相切/相离三种情况 |
| SIR 传染病模型 | 25s | 微分方程数值解 + 群体免疫阈值 |
| 法拉第定律 | 30s | 滑轨动画 + EMF 推导 |
| 特征值与特征向量 | 40s | 矩阵变换 + 网格变形动画 |

### 💻 力扣算法可视化 3 个（图形为主）

> 设计原则：图形占画面 80%+，指针/节点/队列全程动态可见，文字只作小标签

| 案例 | 时长 | 代码 | 内容亮点 |
|------|------|------|----------|
| [#1 Two Sum](examples/leetcode/lc_01_two_sum.py) | 33s | O(n²) → O(n) 对比 | 数组方块高亮 + 暴力双循环 + HashMap 构建动画 + 补数查找连线 |
| [#206 反转链表](examples/leetcode/lc_206_reverse_list.py) | 46s | 迭代三指针 | 5节点链表 + prev/curr/next 指针逐步移动 + 箭头翻转动画 + 节点变色 |
| [#102 层序遍历](examples/leetcode/lc_102_level_order.py) | 32s | BFS + 队列 | 7节点二叉树 + 队列入队出队动画 + 层级颜色区分 + 父子连线 |

### 🏆 2024 高考真题讲解（图形为主，3 道大题）

> 新版设计：图形始终占满画面，文字标签随图形变化，全程无大段文字推导

| 题目 | 时长 | 代码 | 内容亮点 |
|------|------|------|----------|
| [第16题 解析几何(椭圆)](examples/gaokao_2024/gk2024_16_conic.py) | 51s | x²/4+y²/3=1 | 椭圆描点轨迹 + 焦弦连续扫描 + 三角形面积实时计算 + |PF₁|+|PF₂|=2a 演示 |
| [第17题 立体几何](examples/gaokao_2024/gk2024_17_solid.py) | 53s | 正三棱柱 + 圆 | 棱柱3D构建 + 半圆弧D点运动 + Thales定理直角 + 法向量计算 + 360°旋转 |
| [第18题 导数函数](examples/gaokao_2024/gk2024_18_derivative.py) | 71s | f(x)=eˣ−ax−1 | 切线连续扫描 + 单调区间着色 + f(x)≥0证明 + 参数a扫描曲线族 |

---

## 🚀 30 秒快速开始

### 方式 A：Docker（零基础首选，5 分钟内出效果）

```bash
# 克隆项目
git clone https://github.com/bcefghj/math-animation-mcp.git
cd math-animation-mcp

# 一键启动（自动下载依赖）
docker compose up -d

# 打开浏览器
# → http://localhost:7860
```

### 方式 B：Cursor MCP（程序员推荐）

在项目根目录创建 `.cursor/mcp.json`：

```json
{
  "mcpServers": {
    "math-animation": {
      "command": "uvx",
      "args": ["math-animation-mcp"],
      "env": { "OUTPUT_DIR": "./animation_output" }
    }
  }
}
```

重启 Cursor，`Cmd+L` 打开对话直接说话：

```
帮我做一个勾股定理证明动画，适合初中生
@高考数学.pdf 讲解第18题
把这段导数知识点做成动画，黑板风格
```

### 方式 C：pip 安装

```bash
pip install math-animation-mcp
math-animation-mcp --web       # 启动 Web 界面
# → http://localhost:7860
```

---

## 📖 保姆级安装教程

> 完全小白也能看懂，按步骤来，10 分钟搞定

### 第一步：确认你的电脑系统

- **苹果 Mac**（macOS）→ 看下面 [macOS 安装](#macos-安装)
- **Windows 10/11** → 看 [Windows 安装](#windows-安装)
- **Linux（Ubuntu）** → 看 [Linux 安装](#linux-安装)
- **懒得折腾** → 看 [Docker 安装](#docker-安装最懒最稳)（任何系统都行）

---

### macOS 安装

> 适用于 macOS 12 Monterey 及以上（M1/M2/M3 芯片也支持）

**第一步：打开终端**

按 `Command（⌘）+ 空格`，输入「终端」，按回车打开。

**第二步：安装 Homebrew（没有的话）**

把下面这行粘贴到终端，按回车：

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

> 💡 Homebrew 是 macOS 上的软件包管理器，相当于苹果版的「软件商店」，免费。  
> 安装过程需要 5-15 分钟，期间会要求输入电脑密码（输入时屏幕不显示字符，正常的）。

**第三步：安装系统依赖**

```bash
# 安装绘图库和视频工具
brew install cairo pango ffmpeg pkg-config

# 安装中文字体（不装的话中文会显示乱码）
brew install --cask font-noto-sans-cjk
```

> ⏱ 预计耗时：5-10 分钟（取决于网速）

**第四步：安装 Python（建议用 uv 管理）**

```bash
# 安装 uv（现代 Python 包管理器，速度是 pip 的 10-100 倍）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 让终端识别 uv 命令（关闭终端重新打开也行）
source ~/.zshrc
```

**第五步：克隆并安装项目**

```bash
# 下载项目代码
git clone https://github.com/bcefghj/math-animation-mcp.git
cd math-animation-mcp

# 创建虚拟环境并安装（约 5-10 分钟）
uv venv .venv
source .venv/bin/activate
uv pip install -e ".[web,ocr]"
```

**第六步：验证安装**

```bash
# 测试是否安装成功
python -c "import manim; print('Manim OK')"
python -c "from math_animation_mcp.utils.sandbox import render_manim_code; print('MCP OK')"
```

两行都输出 OK 就说明安装成功了！

**第七步：启动！**

```bash
# 启动 Web 界面
python -m math_animation_mcp --web

# 输出类似：Running on local URL: http://127.0.0.1:7860
```

打开浏览器访问 `http://127.0.0.1:7860`，就能用了！

---

### Windows 安装

> 适用于 Windows 10（1903 及以上）/ Windows 11

**第一步：安装 Python**

1. 打开 https://www.python.org/downloads/
2. 点击「Download Python 3.11.x」（选 3.11 或更新版本）
3. **关键**：安装时勾选「✅ Add Python to PATH」
4. 点击「Install Now」

**第二步：安装 Chocolatey（Windows 的软件包管理器）**

以管理员身份打开 PowerShell（开始菜单 → 搜索 PowerShell → 右键「以管理员身份运行」）：

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

**第三步：安装 Manim 和 FFmpeg**

在管理员 PowerShell 中继续：

```powershell
choco install manimce ffmpeg -y
```

> ⏱ 预计耗时：10-20 分钟

**第四步：安装 MiKTeX（LaTeX 环境，用来渲染数学公式）**

1. 打开 https://miktex.org/download
2. 下载并运行安装程序
3. 安装时选择「Install missing packages automatically: Yes」

> ⏱ 预计耗时：10-20 分钟

**第五步：克隆并安装项目**

在普通 PowerShell（不需要管理员）中：

```powershell
git clone https://github.com/bcefghj/math-animation-mcp.git
cd math-animation-mcp
pip install -e ".[web]"
```

**第六步：启动！**

```powershell
python -m math_animation_mcp --web
```

打开浏览器访问 `http://localhost:7860`

---

### Linux 安装

> 适用于 Ubuntu 20.04 / 22.04 / 24.04（Debian 系列）

```bash
# 第一步：安装系统依赖
sudo apt update
sudo apt install -y \
    libcairo2-dev libpango1.0-dev \
    ffmpeg python3-pip python3-venv \
    texlive-full fonts-noto-cjk \
    pkg-config cmake git

# 第二步：克隆项目
git clone https://github.com/bcefghj/math-animation-mcp.git
cd math-animation-mcp

# 第三步：创建虚拟环境
python3 -m venv .venv
source .venv/bin/activate

# 第四步：安装
pip install -e ".[web,ocr]"

# 第五步：启动
python -m math_animation_mcp --web
```

---

### Docker 安装（最懒最稳）

> 什么都不用装，只需要有 Docker。适合任何平台（Mac/Win/Linux）。

**第一步：安装 Docker Desktop**

- Mac：https://www.docker.com/products/docker-desktop/ → 下载 Mac 版 → 双击安装
- Windows：同上，下载 Windows 版
- Linux：`sudo apt install docker.io docker-compose-v2`

**第二步：一键启动**

```bash
git clone https://github.com/bcefghj/math-animation-mcp.git
cd math-animation-mcp
docker compose up -d
```

> 第一次运行会下载镜像，约需 3-8 分钟（视网速）。

**第三步：打开浏览器**

访问 `http://localhost:7860`，直接使用！

**停止服务：**

```bash
docker compose down
```

**更新到最新版：**

```bash
git pull
docker compose up -d --build
```

---

## 🎮 使用教程

### 教程 1：Web 界面生成你的第一个动画

1. 启动服务后，打开浏览器访问 `http://localhost:7860`
2. 在「输入描述」框中输入（中英文都行）：
   ```
   帮我做一个勾股定理的证明动画，适合初中生看，用蓝白配色
   ```
3. 选择「风格」：`three_blue_one_brown`（默认）
4. 选择「质量」：`low`（最快预览，约 15 秒出结果）
5. 点击「生成动画」按钮
6. 等待渲染完成，视频自动在右侧播放
7. 点击「下载」保存到本地

> 💡 **小技巧**：先用 `low` 质量预览，满意后再切到 `medium` 或 `high` 生成高清版

---

### 教程 2：在 Cursor AI 里对话式生成

> 需要先完成 [Cursor MCP 配置](#方式-b-cursor-mcp程序员推荐)

打开 Cursor，`Cmd+L`（Mac）/ `Ctrl+L`（Windows）打开对话，直接输入：

**示例 1：基础动画**
```
帮我做一个展示正弦函数 y=sin(x) 的动画，展示振幅、频率、相位变化
```

**示例 2：高考题讲解**
```
帮我做一个 2025 高考数学第 18 题（椭圆）的讲解动画，
要求：题目先展示 → 一步步求解方程 → 画出椭圆图形 → 动点演示性质
```

**示例 3：上传 PDF**
```
@数学试卷.pdf 帮我讲解第 3 题，可汗学院风格，高中生受众
```

**示例 4：对话修改**
```
（上一个动画太快了）帮我把动画速度调慢一半，字体再大一点
```

---

### 教程 3：直接运行案例代码

项目自带 27 个可直接运行的案例：

```bash
cd math-animation-mcp
source .venv/bin/activate

# 运行 2025 高考第 19 题（导数）讲解
python3 -c "
import sys; sys.path.insert(0, 'src')
from math_animation_mcp.utils.sandbox import render_manim_code

with open('examples/gaokao_2025/gaokao_2025_19_derivative.py') as f:
    code = f.read()

result = render_manim_code(code, quality='low', output_dir='./output')
if result.success:
    print(f'成功！视频保存在: {result.file_path}')
"
```

批量运行所有案例：

```bash
# 运行 15 个基础案例（约 5 分钟）
python examples/basic_math/test_all_cases.py

# 运行 12 个进阶长案例（约 10 分钟）
python examples/basic_math/test_long_cases.py
```

---

### 教程 4：通过命令行 MCP Server 使用

```bash
# 启动 MCP Server（供 AI 工具调用）
python -m math_animation_mcp

# 或者直接用 uvx（无需安装）
uvx math-animation-mcp
```

配合 Claude Desktop 使用，在 `claude_desktop_config.json` 中添加：

```json
{
  "mcpServers": {
    "math-animation": {
      "command": "uvx",
      "args": ["math-animation-mcp"]
    }
  }
}
```

---

## 🛠 常用命令速查

```bash
# 启动 Web 界面
python -m math_animation_mcp --web

# 命令行直接渲染
python -m math_animation_mcp render \
  --text "勾股定理证明" \
  --style three_blue_one_brown \
  --quality medium \
  --output ./my_videos/

# 渲染指定 .py 文件
python -m math_animation_mcp render-file ./my_scene.py

# 查看所有可用模板
python -m math_animation_mcp list-templates

# 检查环境
python -m math_animation_mcp check
```

---

## 🎨 6 种视觉风格

| 风格 | 命令 | 背景 | 适合 |
|------|------|------|------|
| `three_blue_one_brown` | 默认 | 深灰 | 科普、大学 |
| `khan_academy` | `--style khan_academy` | 白色 | 中小学 |
| `textbook` | `--style textbook` | 浅灰 | 正式教材 |
| `playful` | `--style playful` | 暖黄 | 小学低龄 |
| `dark_tech` | `--style dark_tech` | 纯黑 | 竞赛、CS |
| `blackboard` | `--style blackboard` | 深绿 | 模拟课堂 |

对话切换：「换成黑板风格」「用可汗学院配色」

---

## 📐 支持的知识点范围

<details>
<summary>点击展开完整列表</summary>

### 高中数学
- **函数与导数**：指数函数、对数函数、三角函数、导数计算、单调性分析、极值最值
- **圆锥曲线**：椭圆/双曲线/抛物线的方程、焦点性质、离心率、切线
- **立体几何**：棱柱/棱锥/球，线面角、二面角、空间向量法证明
- **数列**：等差/等比、递推数列、数学归纳法
- **概率统计**：古典概型、条件概率、贝叶斯、正态分布、频率直方图

### 高中物理
- **力学**：牛顿定律、抛体运动、圆周运动、简谐振动、弹性势能
- **电磁学**：库仑力、电场线、电势、安培力、电磁感应、法拉第定律

### 大学数学
- **微积分**：极限定义（ε-δ）、导数、积分、泰勒展开、微分方程
- **线性代数**：矩阵运算、行列式、特征值、线性变换、相空间
- **概率论**：随机变量、期望、方差、中心极限定理

### 计算机科学
- 排序算法（冒泡/归并/快排/堆排）
- 数据结构（树、图、哈希表）
- 算法复杂度分析

</details>

---

## 🤖 MCP 工具列表（供 AI 助手调用）

<details>
<summary>展开 21 个工具说明</summary>

| 工具名 | 功能 |
|--------|------|
| `render_animation` | 渲染完整视频（主工具）|
| `preview_scene` | 快速低清预览 |
| `render_gif` | 导出 GIF 动图 |
| `list_templates` | 列出所有预置模板 |
| `get_template` | 获取模板源代码 |
| `search_templates` | 关键词搜索模板 |
| `detect_input_type` | 自动识别输入类型 |
| `parse_pdf` | 解析 PDF 提取公式 |
| `parse_image` | OCR 图片识别数学公式 |
| `fix_ocr_errors` | 修复 OCR 常见错误 |
| `normalize_content` | 结构化内容 |
| `analyze_error` | 分析渲染错误 |
| `fix_latex_error` | 自动修复 LaTeX 错误 |
| `fix_python_error` | 自动修复 Python 错误 |
| `set_style` | 切换视觉风格 |
| `set_preferences` | 更新用户偏好 |
| `get_preferences` | 读取当前设置 |
| `set_branding` | 设置水印和品牌 |
| `export_video` | 格式转换/比例调整 |
| `add_subtitles` | 烧录字幕 |
| `add_tts_narration` | AI 配音（即将推出）|

</details>

---

## ❓ 常见问题 FAQ

**Q：完全不会编程，能用吗？**  
完全可以！Docker + Web 界面，打开浏览器说话就行，不需要写任何代码。

**Q：渲染需要多长时间？**

| 质量 | 30 秒动画耗时 | 建议用途 |
|------|------------|---------|
| low (480p) | 10-30 秒 | 快速预览 |
| medium (720p) | 30-90 秒 | 日常使用 |
| high (1080p) | 2-5 分钟 | 最终输出 |

**Q：中文显示方框或乱码怎么办？**

```bash
# macOS
brew install --cask font-noto-sans-cjk

# Ubuntu
sudo apt install fonts-noto-cjk

# Windows：下载 Noto CJK 字体
# https://www.google.com/get/noto/
```

Docker 版已预装所有字体，不会有这个问题。

**Q：渲染失败了怎么办？**  
系统内置自动修复：失败后自动重试最多 5 次，包括 LaTeX 修复、Python 语法修复。如果仍失败，会降级到预置模板保证出图。

**Q：可以做竖屏短视频版本吗？**

```python
export_video("output.mp4", aspect_ratio="9:16")  # 适合抖音/视频号
```

或对话说：「导出竖屏版，9:16 比例」

**Q：可以加自己的水印吗？**

```python
set_branding(watermark="张老师课堂", intro_text="张老师数学")
```

或对话说：「加个水印，写上"张老师课堂"」

**Q：如何更新到最新版本？**

```bash
cd math-animation-mcp
git pull
source .venv/bin/activate
uv pip install -e . --upgrade
```

---

## 📁 项目结构

```
math-animation-mcp/
├── 📁 src/math_animation_mcp/
│   ├── server.py              # MCP Server（21个工具）
│   ├── web_server.py          # Gradio Web 界面
│   ├── cli.py                 # 命令行入口
│   ├── 📁 tools/              # 工具实现
│   │   ├── render_tools.py    # 渲染
│   │   ├── input_tools.py     # PDF/图片/OCR 处理
│   │   ├── repair_tools.py    # 自动修复
│   │   ├── template_tools.py  # 模板管理
│   │   ├── personalization_tools.py
│   │   └── export_tools.py
│   ├── 📁 templates/          # 预置模板库
│   │   ├── geometry/          # 几何
│   │   ├── algebra/           # 代数
│   │   ├── calculus/          # 微积分
│   │   ├── trigonometry/      # 三角
│   │   ├── statistics/        # 统计概率
│   │   ├── physics/           # 物理
│   │   └── cs/                # 计算机
│   ├── 📁 styles/presets.py   # 6种视觉风格
│   ├── 📁 config/             # 用户偏好
│   └── 📁 utils/              # 沙箱、中文支持、FFmpeg
│
├── 📁 examples/               # ✨ 可运行案例
│   ├── 📁 gaokao_2025/        # 2025 高考真题（3道大题）
│   │   ├── gaokao_2025_17_solid.py      # 立体几何
│   │   ├── gaokao_2025_18_ellipse.py    # 圆锥曲线
│   │   └── gaokao_2025_19_derivative.py # 导数压轴
│   └── 📁 basic_math/         # 基础数学（27个案例）
│       ├── test_all_cases.py            # 15个短案例
│       └── test_long_cases.py           # 12个长案例
│
├── 📁 docs/                   # 详细文档
│   ├── getting-started/
│   ├── tutorials/
│   └── faq/
│
├── 🐳 Dockerfile
├── 🐳 docker-compose.yml
├── 🔧 install.sh              # macOS/Linux 一键安装
├── 🔧 install.ps1             # Windows 一键安装
└── 📄 pyproject.toml
```

---

## 🙏 致谢

- [Manim Community](https://www.manim.community/) — 动画引擎
- [3Blue1Brown](https://www.3blue1brown.com/) — 灵感来源
- [Model Context Protocol](https://modelcontextprotocol.io/) — AI 工具集成标准
- [Gradio](https://gradio.app/) — Web 界面框架

---

## 📄 开源协议

MIT License — 免费用于个人和商业用途，保留版权声明即可。

---

_Made with ❤️ for math education | 让每一道数学题都能被看见_
