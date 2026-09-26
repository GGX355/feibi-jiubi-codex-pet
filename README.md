# 菲比啾比 · Codex 桌宠

一只非官方的《鸣潮》菲比二创桌宠。新版坐着专心打字、托腮等你回应，完成后坐着伸个懒腰。包含九组标准动作和十六方向注视，待机与其他动作保留原版。

## 九组动作动图

| 待机 | 向右跑 | 向左跑 |
| :---: | :---: | :---: |
| ![菲比啾比待机](preview/idle.gif) | ![菲比啾比向右跑](preview/run-right.gif) | ![菲比啾比向左跑](preview/run-left.gif) |

| 挥手 | 跳跃 | 失败·委屈鼓脸 |
| :---: | :---: | :---: |
| ![菲比啾比挥手](preview/waving.gif) | ![菲比啾比跳跃](preview/jump.gif) | ![菲比啾比委屈鼓脸](preview/failed.gif) |

| 等待·坐姿托腮 | 工作·专心打字 | 收工·坐姿伸懒腰 |
| :---: | :---: | :---: |
| ![菲比啾比等待](preview/waiting.gif) | ![菲比啾比工作中](preview/working.gif) | ![菲比啾比坐姿伸懒腰](preview/review.gif) |

## 安装

下载仓库后，将 [`pet`](pet) 文件夹复制到 Windows 的 `%USERPROFILE%\.codex\pets\feibi-jiubi-seated`。该目录中应直接放置 `pet.json` 和 `spritesheet.webp`。若设置了自定义 `CODEX_HOME`，请放进对应的 `pets` 目录。之后在 Codex 的桌宠设置中选择「菲比啾比·坐姿三状态」；必要时重启 Codex 以刷新图集。旧版使用独立的 `feibi-jiubi-chibi` 目录，可以保留并切换。

## 预览

下载仓库后，直接用浏览器打开 [`preview/index.html`](preview/index.html)。页面并排展示九组动作，可逐帧查看、暂停播放、半速观察、按原尺寸查看、切换背景，并拖动滑块查看十六方向注视。网页使用从发布图集直接提取的 PNG 帧，Codex 使用像素一致的无损 WebP。

### Codex 实际播放方式

在本机核对的 Codex `26.924.1866.0` 中，工作动作每轮 820 毫秒，播放三轮（约 2.46 秒）后回到慢速待机，即使任务仍在运行。鼠标交互结束或状态变化可能重新触发动作。`waiting` 表示需要用户输入或批准，`review` 表示完成结果待查看。

本页和 README GIF 为便于观察而持续循环，不代表 Codex 会持续打字。修改 GIF 时长或 `pet.json` 无法改变该版本的原生播放时长。待机和注视仍是站姿，坐姿与站姿直接切换，没有新增起身过渡。后续 Codex 版本的行为可能变化。



| 原生动作 | 本版演出 | 帧数 |
| --- | --- | ---: |
| `idle` | 安静眨眼、闭嘴微笑、双手自然下垂 | 6 |
| `running-right` | 向右小碎步 | 8 |
| `running-left` | 向左小碎步 | 8 |
| `waving` | 打招呼 | 4 |
| `jumping` | 蹦跳 | 5 |
| `failed` | 委屈鼓脸 | 8 |
| `waiting` | 坐着托腮、眨眼等待 | 6 |
| `running` | 坐在电脑前专心打字 | 6 |
| `review` | 坐着闭眼伸懒腰收工 | 6 |
| look directions | 顺时针十六方向 | 16 |

图集为 8 × 11 格、1536 × 2288 像素，每格 192 × 208。`preview/spritesheet.png` 是便于编辑的无损源文件；运行 `python scripts/build_pet.py` 可从它重建 `pet/spritesheet.webp` 并逐像素核对，Codex 加载 WebP 文件。本机按 v2 结构校验通过。预览封面可通过 `python scripts/make_preview.py` 重新生成；九段 GIF、网页 PNG 帧和动作配置脚本可通过 `python scripts/make_action_gifs.py` 从图集和 `preview/actions.json` 重新生成。这些脚本均需 Pillow。

## 声音和后续计划

Codex 原生自定义宠物包只加载图集，不播放仓库自带语音。早期本地预览的社区声音来自不同视频及网站，这里**没有再分发音频**。来源见 [素材说明](ASSET_RIGHTS.md)。随机演出、连点、长按等互动属于计划中的独立桌宠阶段，本仓库当前版本没有实现这些交互。

## 许可与署名

预览网页和构建脚本采用 [MIT License](LICENSE)。角色图像是基于《鸣潮》菲比的二创，不归入 MIT 许可；具体来源和使用边界见 [ASSET_RIGHTS.md](ASSET_RIGHTS.md)。本项目与库洛游戏、OpenAI 没有官方关联。
