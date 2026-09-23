# 菲比啾比 · Codex 桌宠

一只非官方的《鸣潮》菲比二创桌宠。这里发布的是**双臂重绘版**：待机时袖子自然垂下，袖口放宽，手套缩小。包含 Codex 自定义桌宠 v2 图集、九组标准动作和十六方向注视。

![菲比啾比动作预览](preview/cover.png)

![待机动画](preview/idle.gif)

## 安装

下载仓库后，将 [`pet`](pet) 文件夹复制到 Windows 的 `%USERPROFILE%\.codex\pets\feibi-jiubi-chibi`。该目录中应直接放置 `pet.json` 和 `spritesheet.webp`。若设置了自定义 `CODEX_HOME`，请放进对应的 `pets` 目录。之后在 Codex 的桌宠设置中选择「菲比啾比·双臂重绘版」；必要时重启 Codex 以刷新图集。

## 预览

下载仓库后，直接用浏览器打开 [`preview/index.html`](preview/index.html)。页面可切换九组动作、逐帧查看、暂停播放、切换背景，并拖动滑块查看十六方向注视。网页只是素材预览，Codex 原生动作由任务状态和鼠标交互决定。



| 原生动作 | 本版演出 | 帧数 |
| --- | --- | ---: |
| `idle` | 安静眨眼、闭嘴微笑、双手自然下垂 | 6 |
| `running-right` | 向右小碎步 | 8 |
| `running-left` | 向左小碎步 | 8 |
| `waving` | 打招呼 | 4 |
| `jumping` | 蹦跳 | 5 |
| `failed` | 委屈鼓脸 | 8 |
| `waiting` | 搓手等待 | 6 |
| `running` | 认真开工 | 6 |
| `review` | 得意点头 | 6 |
| look directions | 顺时针十六方向 | 16 |

图集为 8 × 11 格、1536 × 2288 像素，每格 192 × 208。`preview/spritesheet.png` 是便于编辑的无损源文件；运行 `python scripts/build_pet.py` 可从它重建 `pet/spritesheet.webp` 并逐像素核对，Codex 加载 WebP 文件。本机按 v2 结构校验通过。预览封面可通过 `python scripts/make_preview.py` 重新生成。两段脚本均需 Pillow。

## 声音和后续计划

Codex 原生自定义宠物包只加载图集，不播放仓库自带语音。早期本地预览的社区声音来自不同视频及网站，这里**没有再分发音频**。来源见 [素材说明](ASSET_RIGHTS.md)。随机演出、连点、长按等互动属于计划中的独立桌宠阶段，本仓库当前版本没有实现这些交互。

## 许可与署名

预览网页和构建脚本采用 [MIT License](LICENSE)。角色图像是基于《鸣潮》菲比的二创，不归入 MIT 许可；具体来源和使用边界见 [ASSET_RIGHTS.md](ASSET_RIGHTS.md)。本项目与库洛游戏、OpenAI 没有官方关联。
