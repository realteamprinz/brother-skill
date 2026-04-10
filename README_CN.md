<div align="center">

# brother.skill

> "你的兄弟退出了群聊，现在没人记得为什么我们叫Dave'那个事件'。
> 你最爱的主播被封了，三年的梗都跟着一起消失了。
> 你的网友突然消失了，唯一的痕迹是一个已注销的Discord账号。
> 把冰冷的告别变成温暖的Skill——欢迎来到兄弟永生！"

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Claude Code Skill](https://img.shields.io/badge/Claude_Code-Skill-orange.svg)](https://docs.anthropic.com)
[![AgentSkills Standard](https://img.shields.io/badge/AgentSkills-Standard-green.svg)](https://github.com/NousResearch/hermes-agent)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Ready-brightgreen.svg)](https://clawhub.ai/realteamprinz/brother)

[English](README.md) · [Español](README_ES.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Português](README_PT.md)

</div>

---

**蒸馏你的兄弟们。** 那些能让你笑到缺氧的人。线上线下都算——只要是你的兄弟，这个skill全都记住。

提供素材（YouTube视频、TikTok短视频、Twitch直播、Discord聊天记录、微信截图、群聊导出、抖音、B站、飞书、钉钉、QQ聊天记录）再加上你自己对这个人的描述，就能得到一个 **说话真的像他们的AI Skill**。

## 支持的来源

| 来源 | 格式 | 能捕捉到什么 |
|------|------|-------------|
| YouTube | 视频链接或字幕文件 | 说话风格、口头禅、能量值、幽默节奏 |
| TikTok / 抖音 | 视频链接或保存的片段 | 短视频能量、名场面、反复出现的梗 |
| Twitch | 切片链接或VOD时间戳 | 直播反应、和弹幕互动的方式、暴怒名场面 |
| X / Twitter | 主页链接或推文导出 | 文字风格、毒舌吐槽、被喷时的反应 |
| Discord | 聊天记录导出（.json） | 实时互怼、表情包使用习惯、群内生态位 |
| 微信 | 截图或聊天记录导出 | 中文互联网梗、表情包、语音消息风格 |
| Bilibili（B站） | 视频链接或弹幕导出 | 弹幕文化、鬼畜能量、经典语录 |
| 飞书 | 聊天记录导出 | 职场整活、阴阳怪气、已读不回的艺术 |
| 钉钉 | 聊天记录导出 | 打工人能量、加班吐槽、DING一下的恐惧 |
| QQ | 聊天记录导出 | 远古互联网记忆、QQ秀审美、经典表情 |
| 群聊（通用） | 任意平台的文字导出 | 多人互动、内部梗、每个人的角色 |
| 手动描述 | 你自己的话 | 任何你记得的——故事、印象、名场面 |

## 安装

```bash
# OpenClaw
clawhub install realteamprinz/brother

# Hermes
hermes skills install brother-skill

# Claude Code
cp -r brother-skill/ ~/.claude/skills/

# Python（用于蒸馏流水线）
git clone https://github.com/realteamprinz/brother-skill.git
cd brother-skill
pip install -r requirements.txt
```

## 快速开始

### 从YouTube蒸馏

```bash
python distill.py --source youtube --url "https://youtube.com/watch?v=..." --name "Jake Paul"
```

### 从B站蒸馏

```bash
python distill.py --source bilibili --url "https://bilibili.com/video/BV..." --name "何同学"
```

### 从Discord聊天记录蒸馏

```bash
python distill.py --source discord --file chat_export.json --name "Dave"
```

### 从微信聊天记录蒸馏

```bash
python distill.py --source wechat --file wechat_export.json --name "老王"
```

### 从群聊蒸馏

```bash
python distill.py --source groupchat --file groupchat.txt --names "张三,李四,王五"
```

### 从你自己的描述蒸馏

```bash
python distill.py --source manual --name "我的兄弟小明"
```

进入交互模式——描述你的兄弟，skill会自动构建他的档案。

## 示例

### Jake Paul

> "Jake Paul会怎么评价我今天很倒霉？"
>
> "兄弟。倒霉？我们不接受倒霉这个设定。你知道我们怎么办吗？买一台兰博基尼然后直接碾过去。IT'S EVERYDAY BRO。"

### Logan Paul

> "我该不该开个播客？"
>
> "兄弟。谁都有播客。但不是谁都有IMPAULSIVE。你的hook是什么？……算了直接开吧。想那么多干嘛。我当初就是这么干的。"

### MrBeast

> "怎么才能涨粉？"
>
> "换封面。不我认真的。你试过发十万块钱吗？这招一般都管用。还有你的标题得让人不点就难受。"

### 张凤霞

> "张凤霞会怎么讲今天上班迟到的事？"
>
> "你们听我说啊！！今天——我迟到了。【停顿三秒】但是！这不是一个普通的迟到！这是一场命运的考验！！先是闹钟没响，然后公交跑了，然后——你们猜怎么着——下！雨！了！我跟你们说我站在雨里的那一刻，我觉得整个世界都在针对我。【突然笑】但是后来老板也迟到了哈哈哈哈哈！"

### 李子柒

> "李子柒会怎么回应压力大？"
>
> "……（安静地走到院子里，摘了一篮子花椒）有些事情急不来的。你看这个酱，要晒够180天才能用。日子也是一样。慢慢来。先吃饭吧，今天做了腊肉炒蕨菜。"

### 罗翔

> "罗翔老师怎么看我今天被人插队？"
>
> "关于插队这个问题啊，我给大家讲一个案例。张三——又是张三——他在食堂插队，结果被后面的人泼了一碗汤。那么问题来了：泼汤的人构不构成故意伤害罪？【台下笑】大家先别笑，这个问题其实涉及到正当防卫的边界。当然了，最好的解决方案是——我们做一个内心平静的人。但张三不会。张三永远不会。"

### 何同学

> "何同学会怎么评价我的桌面布局？"
>
> "OK我仔细看了一下你的桌面。说实话，想法是有的，但是——线材管理需要再想想。我之前花了大概两周时间研究过最优的桌面布线方案，最后发现一个反直觉的结论：最好的线材管理就是——减少线材。所以我的建议是先问自己一个问题：桌面上每一个东西，真的需要在那里吗？对了这个显示器支架不错，链接我放评论区了。"

### 你们的群聊

> "写一下我们群里在策划团建"
>
> **老王：** 周末团建 谁来
> **小李：** 去哪
> **老王：** 不知道 找个好玩的地方
> **小李：** 这不是计划
> **张伟：** [发了个表情包]
> **老王：** 张伟你到底来不来
> **张伟：** [又发了个表情包]
> **小李：** 我可以开车 但有人得出油钱
> **老王：** 哥你开新能源的
> **小李：** 对啊 所以有人得出充电钱
> **张伟：** 建议AA 我先退群了

## 兄弟原型

brother.skill 能识别不同的兄弟类型：

| 原型 | 描述 | 典型代表 |
|------|------|---------|
| **大气层制造机** | 能量拉满，永远在尖叫，把什么事都搞成大事件 | IShowSpeed / PDD |
| **毒舌王** | 精准到位的吐槽，面不改色地把你怼到自闭 | KSI / 罗翔（优雅版） |
| **酷哥** | 佛系能量，很少说话，但一开口全场安静 | 基努里维斯 / 李子柒 |
| **混沌制造者** | 做一些没人让他做的事，但结果居然还行 | Jake Paul / 药水哥 |
| **战略大脑** | 把什么都变成商业计划或者人生道理 | MrBeast / 何同学 |
| **沉默杀手** | 安静了20分钟然后来一句话直接团灭 | 每个群里都有一个，你知道是谁 |
| **表情包战神** | 只用表情包和梗图交流 | 每个群聊里的那位 |
| **故事大王** | 任何经历到他嘴里都变成十分钟的沉浸式大戏 | 张凤霞 / 你最能扯的那个朋友 |

## 工作原理

```
素材输入                 蒸馏流水线                  兄弟档案
────────                ──────────                 ────────
YouTube视频      ──┐                                ┌── 语言与说话方式
TikTok/抖音      ──┤                                ├── 搞笑风格
Twitch直播       ──┤    ┌─────────────────┐        ├── 能量与氛围
Discord记录      ──┼──► │  BroDistiller   │ ─────► ├── 内容人格
微信导出         ──┤    │  ProfileBuilder │        ├── 群内角色
B站/飞书/钉钉    ──┤    │  ArchetypeDetect│        ├── 兄弟原型
群聊记录         ──┤    └─────────────────┘        └── 关系定位
你的描述         ──┘                                   + 互动模式
```

1. **喂素材** —— 视频切片、截图、故事、群聊记录、你的描述
2. **BroDistiller** 处理所有素材，提取原始信号
3. **ProfileBuilder** 把数据整理成五个维度（语言、搞笑、能量、内容、关系）
4. **ArchetypeDetect** 把你的兄弟归类到8种原型之一
5. **档案保存** —— 一份活的文档，每次新输入都会更深入
6. **互动模式** —— 用他们的声音、他们的黑话、他们的能量跟你的兄弟对话

## 兄弟档案维度

每个兄弟会从五个维度建立档案：

### 语言与说话方式
口头禅、黑话、说话习惯、音量等级、招牌损人句式、偶尔的表扬（很罕见）。

### 搞笑风格
幽默类型、节奏感、招牌操作、永远会开玩笑的话题、绝对不碰的话题。

### 能量与氛围
默认能量等级、嗨点触发器、群内角色、进群时的气场。

### 内容人格（线上兄弟）
主要平台、内容风格、粉丝互动方式、联动化学反应、成长变化轨迹。

### 和你的关系
你们怎么认识的、内部梗、最经典的时刻、丧尸末日生存搭档评分。

## 隐私与数据

- **所有数据存储在本地** `~/.brother-skill/bros/`
- **没有云同步。** 没有外部传输。零数据离开你的设备。
- **你控制一切。** 删除任何兄弟档案只需删除对应文件夹。
- **尊重蒸馏。** 捕捉能量和幽默，而不是私人信息。

## 家族成员

**日常系列：**
- [mom.skill](https://clawhub.ai/realteamprinz/mom) — 妈妈的育儿副驾驶
- [dad.skill](https://clawhub.ai/realteamprinz/dad) — 爸爸的育儿副驾驶
- **brother.skill** — 蒸馏你的兄弟们 *（你在这里）*

**传承系列：**
- [mother.skill](https://clawhub.ai/realteamprinz/mother) — 保存妈妈的智慧
- [father.skill](https://clawhub.ai/realteamprinz/father) — 保存爸爸的精神
- [grandma.skill](https://clawhub.ai/realteamprinz/grandma) — 奶奶/外婆的故事和菜谱
- [grandpa.skill](https://clawhub.ai/realteamprinz/grandpa) — 爷爷/外公的故事和力量

**宠物系列：**
- [paw.skill](https://clawhub.ai/realteamprinz/paw) — 蒸馏你宠物的灵魂
- [dog.skill](https://clawhub.ai/realteamprinz/dog) — 犬类智能
- [cat.skill](https://clawhub.ai/realteamprinz/cat) — 猫类智能

**财富系列：**
- [midas.skill](https://clawhub.ai/realteamprinz/midas) — 提取财富系统

## 贡献

1. Fork 这个仓库
2. 创建你的分支（`git checkout -b feature/new-source`）
3. 在 `src/sources/` 里添加你的来源处理器
4. 在 `tests/` 里写测试
5. 提交 PR

欢迎新的来源类型、更好的原型检测、以及多语言改进。

## 许可证

MIT 许可证。详见 [LICENSE](LICENSE)。

---

> *"我们蒸馏时间带走的一切。"* —— 但有时候我们也蒸馏那些让我们笑到流泪的东西。
>
> 由 [@realteamprinz](https://github.com/realteamprinz) 构建 | [PRINZCLAW](https://prinzclaw.ai)
