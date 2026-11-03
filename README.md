<div align="center">

# Anthropic Calm UI

**受 Anthropic / Claude 界面启发的前端设计 Skill**

清晰的排版 · 舒适的阅读节奏 · 克制的交互

[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)
[![Validate skill](https://github.com/ayahana/anthropic-calm-ui/actions/workflows/validate.yml/badge.svg)](https://github.com/ayahana/anthropic-calm-ui/actions/workflows/validate.yml)
[![Agent Skills](https://img.shields.io/badge/Agent_Skills-SKILL.md-black?style=flat-square)](skills/anthropic-calm-ui/SKILL.md)

[设计特点](#设计特点) · [安装](#安装) · [快速上手](#快速上手) · [参与贡献](#参与贡献)

</div>

## 项目简介

Anthropic Calm UI 为 AI 编程助手提供前端设计指导，支持从零制作网站、改进现有界面，以及评审页面和组件。

它从 Anthropic / Claude 的公开界面中提炼内容层级、排版节奏与交互方式，帮助 AI 根据你的产品任务做设计选择。内容站可以舒展，工作台可以紧凑，鲜明的品牌色和深色主题也可以保留。

技能以中文编写，沿用项目已有的框架、组件和设计系统。使用指导本身无需 API 密钥、额外服务或字体下载。

## 设计特点

- **先安排内容，再决定外观。** 从读者要理解的信息、用户要完成的任务出发，组织页面结构与主要操作。
- **让排版形成层级。** 用字号、字重、对齐和间距区分主次，兼顾中文长标题、正文阅读和中英混排。
- **保留产品自己的性格。** 按品牌选择颜色和字体，按任务选择信息密度，支持浅色与深色界面。
- **让交互清楚可用。** 关注键盘焦点、加载与错误反馈、窄屏布局，以及实际前景和背景的色彩对比。

### 可以用在哪些地方？

| 场景 | 设计重点 |
| --- | --- |
| 官网、博客、内容站 | 标题层级、正文行宽、章节节奏与清楚的行动入口 |
| 产品介绍、品牌页面 | 保留品牌色与图片，让产品信息和主要操作更突出 |
| 工作台、数据后台 | 紧凑的布局、易扫读的表格与稳定的工具栏 |
| 表单、弹窗、移动组件 | 清晰标签、状态反馈、触控与键盘操作 |
| 现有界面评审 | 找出具体的阅读和操作问题，给出范围明确的改进建议 |

更多设计取舍见 [场景示例](skills/anthropic-calm-ui/references/patterns.md)。

## 安装

### 方式一：使用 skills CLI

需要 Node.js 22.20 或更高版本，详见 [skills CLI 官方说明](https://github.com/vercel-labs/skills#install-a-skill)。在你的项目目录运行：

```sh
npx skills add ayahana/anthropic-calm-ui --skill anthropic-calm-ui
```

按提示选择要安装到的 AI 编程助手。默认安装到当前项目；需要跨项目使用时，在命令末尾加上 `-g`。

### 方式二：手动复制

克隆仓库，或在 GitHub 点击 **Code → Download ZIP** 下载：

```sh
git clone https://github.com/ayahana/anthropic-calm-ui.git
```

将仓库中的 `skills/anthropic-calm-ui/` 整个文件夹复制到客户端配置的技能目录，保留 `SKILL.md`、`references/` 和 `scripts/`。客户端的具体路径可查阅 [skills CLI 的 Agent 目录参考](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)。

安装后，在客户端的技能列表中确认出现 `anthropic-calm-ui`，再尝试下面的请求。各客户端的发现与启用方式以其实际版本为准。

## 快速上手

安装后，在 AI 编程助手中指定技能名称并描述需求。支持 `$技能名` 的客户端可以直接复制以下示例：

**从零做一个网站**

```text
使用 $anthropic-calm-ui 做一个中文科技博客首页，蓝色品牌，重点展示文章和专题。
```

**改进现有页面**

```text
使用 $anthropic-calm-ui 改善当前后台的排版和表格层级，保留侧栏、品牌色和现有功能。
```

**只评审，不改代码**

```text
使用 $anthropic-calm-ui 评审当前页面，给出最值得改的三点，先不修改代码。
```

附上当前页面截图、已有代码或真实内容，可以让建议更贴合你的项目。不支持 `$` 调用的客户端可直接指定技能名，或让助手读取 [SKILL.md](skills/anthropic-calm-ui/SKILL.md)。

## 技能里有什么？

| 内容 | 用途 |
| --- | --- |
| [SKILL.md](skills/anthropic-calm-ui/SKILL.md) | 技能入口与设计工作方式 |
| [场景示例](skills/anthropic-calm-ui/references/patterns.md) | 内容站、商店、创作工具与后台的设计取舍 |
| [示例 CSS](skills/anthropic-calm-ui/references/tokens.css) | 可选的浅色 / 深色变量、字体回退与基础样式 |
| [配色检查](skills/anthropic-calm-ui/references/validation.md) | 示例颜色的对比值与检查脚本用法 |
| [观察笔记](skills/anthropic-calm-ui/references/evidence.md) | 风格来源与历史页面观察 |

示例 CSS 可按需映射到项目现有变量中。实际界面效果取决于内容、实现与验证；当前仓库的场景演练为文字方案，尚未提供渲染后的页面截图，详见 [验证记录](VALIDATION.md)。

## 参与贡献

欢迎改进设计指导、中文排版与场景示例。提交前请阅读 [贡献指南](CONTRIBUTING.md)。

维护配色或检查脚本时，在仓库根目录运行以下命令，需要 Python 3.9 或更高版本，无第三方 Python 依赖：

```sh
python -m unittest discover -s tests -v
python scripts/check_contrast.py
```

## 许可证

[MIT License](LICENSE) © 2026 ayahana。

本项目为独立、非官方 Skill，未获 Anthropic 背书。示例样式为独立适配建议；Anthropic / Claude 的品牌、字体和其他第三方内容不包含在本项目的许可中。详细来源见 [PROVENANCE.md](PROVENANCE.md)。
