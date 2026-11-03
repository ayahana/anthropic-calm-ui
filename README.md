# Anthropic-inspired Calm UI

中文优先、跨领域的独立前端设计 Skill。面向不同网站、应用和组件的新建、重设计、局部调整与评审，将公开 Anthropic / Claude 界面所启发的清晰层级、阅读节奏、内容优先和克制交互，适配到用户自己的产品。

技能目录和调用名为 `anthropic-calm-ui`。按产品任务、品牌与设备调整表达，保留平静、人文的设计方向，不把所有项目变成同一套米白模板。

**非官方项目。** 未获得 Anthropic 背书，不是官方 frontend-design Skill 的副本，不提供品牌复刻、官方字体或商标素材。名称只描述研究来源。

## 适用场景

- 从零建内容站或产品网站：从受众与内容结构决定页面、导航和阅读节奏。
- 品牌营销、消费产品：保留鲜明品牌与产品图片，让主要信息和行动更清楚。
- 生产力工具、多页后台：按任务选择密度，验证跨页路径与状态，不把工作区做成宣传页。
- 移动界面与组件局部改进：兼顾软键盘、安全区、交互状态和原有业务约束。
- 仅评审：给出有依据的改进建议与未验证项，不擅自修改项目。

保留现有框架、设计系统、品牌色与业务流程。浅色和深色 token 都是独立建议，**不等于原站测量或原站主题行为**。不需要依赖、联网字体、API 密钥或后台服务。

## 安装

技能本体在 `skills/anthropic-calm-ui/`，包含 `SKILL.md`、`references/` 与零依赖的 `scripts/`。将整个文件夹复制到你使用的工具所支持的技能目录，保留子目录。安装位置和发现方式以该工具当前说明为准；本仓库不执行安装或修改配置。

如果使用支持 `$技能名` 的客户端，可以这样请求：

> 使用 $anthropic-calm-ui 从零设计一个蓝色品牌的中文内容网站，包含首页、专题和文章页。保持清晰、克制的阅读体验，不加账户或支付，沿用当前项目技术栈。

> 使用 $anthropic-calm-ui 检查当前页面。保留框架、侧栏、品牌色和业务流程，只提出三项改善建议，不改代码。

> 使用 $anthropic-calm-ui 改善这个深色确认弹窗。只改当前组件，复用已有变量，不新增依赖，验证焦点、长中文和失败状态。

若客户端未发现技能，可直接提供 `SKILL.md` 及它按需引用的文件。未在所有第三方客户端逐一安装测试。

## 仓库结构

- `skills/anthropic-calm-ui/SKILL.md`：触发范围、设计决策与交付边界。
- `skills/anthropic-calm-ui/references/`：历史来源、适配案例、可选 token 与验证边界。
- `skills/anthropic-calm-ui/scripts/check_contrast.py`：随技能安装的配色回归检查；仓库 `scripts/check_contrast.py` 仅作入口，避免复制实现。
- `tests/`：验证计算和失败路径的测试。
- `CONTRIBUTING.md`：贡献与来源要求。
- `PROVENANCE.md`：素材来源与授权边界。
- `RELEASE_CHECKLIST.md`：发布前确认项。

## 验证

需要 Python 3.9 或更高版本，无第三方依赖：

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_contrast.py
python3 scripts/check_contrast.py --json
```

脚本直接读取 CSS 中的实色 token，检查两主题共 52 组前景/背景；低于门槛退出码为 1，缺失、重复受测 token 或不支持的颜色输入退出码为 2。它不是通用 CSS 解析器，不解析变量、透明度、渐变或层叠。改了 CSS 语法需要同时维护测试，不要忽略失败。

已测试技能文件夹脱离仓库后能运行配色脚本，但这不等于第三方客户端安装或发现测试。六类文字场景演练检查相应回答的范围控制与跨领域适配，不是实际 UI 效果验证或 A/B 盲评。详见 [验证记录](VALIDATION.md)。

仓库提供 GitHub Actions 配置；本地运行成功不代表远程 CI 已执行。无需网页构建步骤，因为交付物是指导 Skill，不是组件库或完整应用。

## 证据与限制

桌面公共页面的历史观察保留在 [观察笔记](skills/anthropic-calm-ui/references/evidence.md)，原始截图未随包提供，本次上传检查未重新执行官网视觉观察。2026-11-03 的历史主题记录描述：dark 媒体查询为 true 时，Claude 官网呈现深色，Anthropic 公司首页为浅色主体与深色页脚分区；第一轮未记录媒体查询，因此不构成完整受控双状态实验。详见 [主题复核记录](skills/anthropic-calm-ui/references/theme-behavior.md)。这些记录不能证明网站当前外观，也不覆盖登录后工作区、原生 App、手机布局或完整键盘与读屏行为。

## 许可证

本项目的独立编写内容采用 [MIT License](LICENSE)，版权署名为 ayahana。Anthropic / Claude 的品牌、网站、字体和其他第三方内容不因本项目的许可证而获得授权。素材来源与适用范围见 [PROVENANCE.md](PROVENANCE.md)。
