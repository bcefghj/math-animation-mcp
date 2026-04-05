# 你的第一个数学动画

本教程手把手教你从零创建一个数学动画。

## 准备工作

确保你已经安装了 math-animation-mcp（参见 README）。

## 方式 1：通过 Web 界面（最简单）

1. 启动 Web 界面：
   ```bash
   math-animation-mcp --web
   ```

2. 打开浏览器访问 http://localhost:7860

3. 在代码编辑器中，你会看到一个示例代码。点击「快速预览」看看效果。

4. 试试从「模板库」选项卡中选择一个模板：
   - 点击分类下拉框，选择 `geometry`
   - 在模板 ID 输入框中输入 `geometry/pythagorean`
   - 点击「加载模板代码」

5. 把加载的代码复制到代码编辑器中，点击「渲染」。

## 方式 2：通过 Cursor（推荐日常使用）

1. 确保 `.cursor/mcp.json` 已配置（见 README）

2. 在 Cursor 中新建对话，输入：
   ```
   帮我做一个勾股定理的证明动画
   ```

3. AI 会自动：
   - 搜索匹配的模板
   - 生成 Manim 代码
   - 预览渲染
   - 返回视频文件

4. 如果需要调整，直接说：
   ```
   字再大一点，动画慢一些
   ```

## 方式 3：直接写 Python 代码

创建一个 `my_first_animation.py` 文件：

```python
from manim import *

class MyFirstAnimation(Scene):
    def construct(self):
        # 标题
        title = Text("我的第一个动画", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # 欧拉公式
        formula = MathTex(r"e^{i\pi} + 1 = 0", font_size=64, color=YELLOW)
        self.play(Write(formula))
        self.wait(1)

        # 高亮各部分
        box = SurroundingRectangle(formula, color=RED)
        self.play(Create(box))
        self.wait(1)

        # 最美公式
        beauty = Text("最美丽的数学公式", font_size=36, color=BLUE)
        beauty.next_to(formula, DOWN, buff=0.5)
        self.play(Write(beauty))
        self.wait(2)
```

然后渲染：

```bash
manim -qm my_first_animation.py MyFirstAnimation
```

生成的视频在 `media/videos/` 目录下。

## 下一步

- 浏览[模板库](../tutorials/basic-math-animation.md)学习更多动画技巧
- 尝试[自定义风格](../tutorials/customize-style.md)
- 学习[处理 PDF 试卷](../tutorials/pdf-to-animation.md)
