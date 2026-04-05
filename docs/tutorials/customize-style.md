# 自定义风格

## 切换风格预设

在 Cursor 中对话：

```
设置风格为可汗学院
```

或使用 MCP 工具：

```
set_style("khan_academy")
```

可用风格：`three_blue_one_brown`、`khan_academy`、`textbook`、`playful`、`dark_tech`、`blackboard`

## 设置受众级别

```
设置受众为初中生
```

级别对照：
- 1 = 小学
- 2 = 初中
- 3 = 高中
- 4 = 大学
- 5 = 竞赛

## 自定义偏好

创建 `manim_prefs.yaml`：

```yaml
style:
  preset: "khan_academy"
  custom_colors:
    primary: "#1865F2"
    secondary: "#14BF96"
    accent: "#FF914D"

audience:
  level: 2
  language: "zh-CN"

output:
  default_quality: "medium"
  default_format: "mp4"
  aspect_ratio: "16:9"

animation:
  speed_multiplier: 0.7
  pause_between_steps: 1.5
  font_scale: 1.3

branding:
  watermark: "我的数学课堂"
```

## 添加品牌标识

```
设置水印为"我的数学课堂"
```

支持：水印文字、Logo 图片、片头文字、片尾文字。

## 竖屏输出（手机/抖音）

```
导出为竖屏格式
```

或：

```
export_video(file_path, format="mp4", aspect_ratio="9:16")
```
