<div align="center">

# brother.skill

> "仲間がグループチャットを抜けて、なぜDaveを『あの事件』と呼ぶのか誰も覚えていない。
> 推しの配信者がBANされて、3年分の内輪ネタが一緒に消えた。
> ネッ友が突然消えて、残ったのは削除されたDiscordアカウントだけ。
> 冷たい別れを温かいSkillに変えよう——ブラザー不滅へようこそ！"

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Claude Code Skill](https://img.shields.io/badge/Claude_Code-Skill-orange.svg)](https://docs.anthropic.com)
[![AgentSkills Standard](https://img.shields.io/badge/AgentSkills-Standard-green.svg)](https://github.com/NousResearch/hermes-agent)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Ready-brightgreen.svg)](https://clawhub.ai/realteamprinz/brother)

[English](README.md) · [中文](README_CN.md) · [Español](README_ES.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Português](README_PT.md)

</div>

---

**あなたの"ブラザー"を蒸留しよう。** 息ができなくなるほど笑わせてくれるあいつら。オンラインでもオフラインでも——あなたのブラザーなら、このSkillがすべてを覚えています。

ソース素材（YouTubeクリップ、TikTok動画、Twitch配信、Discordログ、LINEスクリーンショット、グループチャットエクスポート）とあなた自身の説明を提供するだけで、**本当にその人らしく話すAI Skill**が完成します。

## 対応ソース

| ソース | フォーマット | キャプチャされる要素 |
|--------|------------|---------------------|
| YouTube | 動画URLまたはトランスクリプト | 話し方、口癖、テンション、笑いのタイミング |
| TikTok / Douyin | 動画URLまたは保存済みクリップ | ショート動画のエネルギー、バズった瞬間、定番ネタ |
| Twitch | クリップURLまたはVODタイムスタンプ | ライブリアクション、チャット対応スタイル、キレ芸 |
| X / Twitter | プロフィールURLまたはツイートエクスポート | 文体、辛辣なツッコミ、リプライ芸 |
| Discord | チャットログエクスポート (.json) | リアルタイムの掛け合い、ミーム使用、グループの空気感 |
| LINE | スクリーンショットまたはトーク履歴エクスポート | スタンプ文化、既読スルー芸、グループの温度感 |
| ニコニコ動画 | 動画URLまたはコメントログ | 弾幕コメント文化、ネタ、コミュニティの空気 |
| note | 記事URLまたはテキストエクスポート | 長文の語り口、価値観、個性的な文体 |
| WeChat | スクリーンショットまたはチャットエクスポート | 中国ネット文化のユーモア、ミーム、ボイスメッセージのスタイル |
| グループチャット（汎用） | 任意のプラットフォームからのテキストエクスポート | 複数人のダイナミクス、内輪ネタ、役割分担 |
| 手動入力 | あなた自身の言葉 | あなたが覚えていること全部——エピソード、印象、名場面 |

## インストール

```bash
# OpenClaw
clawhub install realteamprinz/brother

# Hermes
hermes skills install brother-skill

# Claude Code
cp -r brother-skill/ ~/.claude/skills/

# Python（蒸留パイプライン用）
git clone https://github.com/realteamprinz/brother-skill.git
cd brother-skill
pip install -r requirements.txt
```

## クイックスタート

### YouTubeから蒸留

```bash
python distill.py --source youtube --url "https://youtube.com/watch?v=..." --name "HIKAKINさん"
```

### Discordログから蒸留

```bash
python distill.py --source discord --file chat_export.json --name "Dave"
```

### グループチャットから蒸留

```bash
python distill.py --source groupchat --file groupchat.txt --names "たけし,ゆうき,けんた"
```

### 手動入力で蒸留

```bash
python distill.py --source manual --name "親友のたけし"
```

インタラクティブモードが起動します——あなたのブラザーについて語ると、Skillがプロフィールを構築します。

## 使用例

### HIKAKINさん

> 「今日のプレゼンめっちゃ緊張するんだけど」
>
> 「大丈夫！大丈夫！ブンブン！ハローYouTube！ ……じゃなくて、ハロープレゼン！ちゃんと準備したならきっとうまくいくよ！僕も最初の動画めっちゃ緊張したけど、やってみたら楽しかったから！ファイト！」

### はじめしゃちょー

> 「新しい趣味始めたいんだけど何がいい？」
>
> 「趣味？ とりあえずスライム1000個買って風呂に入ろう。え？ 普通の趣味がいい？ じゃあ100kgのグミ作ろう。……まじめに言うと、面白そうと思ったことを全部やればいいんだよ。失敗しても動画にすればコンテンツだから。」

### 東海オンエア

> 「来週の飲み会の幹事やることになったんだけど」
>
> **てつや:** よし、企画書作れ。検証動画風にしよう
> **しばゆー:** 場所は俺が決める。（謎の高級店を予約する）
> **りょう:** 予算オーバーだろそれ
> **としみつ:** 俺DJ持っていくわ
> **ゆめまる:** とりあえず寝てていい？
> **虫眼鏡:** ……まず日程調整しない？

### フワちゃん

> 「最近モチベーション上がらないんだよね」
>
> 「はあああああ！？ モチベーション！？ そんなもん最初からないわ！！！ あたし毎日テンションだけで生きてんのよ！！！ とりあえず叫べ！！ AHHHHHH！！ ほら元気出た！！！ 出てないなら音量上げろ！！！」

### MrBeast

> 「再生数を増やすにはどうしたらいい？」
>
> 「サムネを変えろ。いやマジで。あと10万円プレゼント企画やってみた？ だいたいうまくいくよ。あとタイトルは"クリックしないとヤバい"って思わせないとダメ。」

### あなたのグループチャット

> 「うちのグループチャットで旅行計画してるところ書いて」
>
> **たけし:** おい来週旅行行かね？
> **ゆうき:** どこ？
> **たけし:** どっかいいとこ
> **ゆうき:** それプランじゃねえよ
> **けんた:** [スタンプ送信]
> **たけし:** けんた行くの行かないの
> **けんた:** [スタンプ送信]
> **ゆうき:** 運転はするけどガソリン代誰か出して
> **たけし:** お前プリウスじゃん
> **ゆうき:** だから。充電代誰か出して

## ブラザーアーキタイプ

brother.skillは様々なブラザータイプを認識します：

| アーキタイプ | 説明 | 有名な例 |
|---|---|---|
| **盛り上げ番長** | 最大テンション、常に叫んでる、すべてをイベントにする | IShowSpeed |
| **イジリの達人** | 外科的精度のイジリを真顔で繰り出す | KSI |
| **クールブラザー** | 落ち着いたエネルギー、めったに話さないが、話すと全員が聞き入る | Keanu Reeves |
| **カオスエージェント** | 誰も頼んでないことをやる、なぜか成功する | はじめしゃちょー |
| **戦略ブラザー** | すべてをビジネスプランか人生訓に変換する | MrBeast |
| **沈黙の殺し屋** | 20分黙ってて一言で全員を破壊する | あの友達。わかるだろ。 |
| **ミームの帝王** | コミュニケーション手段がミームとリアクション画像のみ | どのグルチャにも一人いる |
| **語り部** | すべての体験が10分間の大河ドラマになる | 一番おもしろい友達 |
| **最大音量系** | ルール無視、全力テンション、とにかく叫ぶ | フワちゃん |
| **みんなのお兄ちゃん** | 親しみやすさ全開、安心感、みんなの最初の推し | HIKAKINさん |

## 仕組み

```
ソース素材             蒸留パイプライン              ブラザープロフィール
────────             ──────────────              ──────────────
YouTubeクリップ  ──┐                                 ┌── 声と言語
TikTok動画      ──┤                                 ├── 笑いのスタイル
Twitch配信      ──┤    ┌─────────────────┐         ├── エネルギーと雰囲気
Discordログ     ──┼──► │  BroDistiller   │ ──────► ├── コンテンツの個性
LINEトーク      ──┤    │  ProfileBuilder │         ├── グループでの役割
ニコニコ動画     ──┤    │  ArchetypeDetect│         ├── アーキタイプ
Twitterポスト   ──┤    └─────────────────┘         └── 関係性
グループチャット ──┤                                     + インタラクションモード
あなたの言葉    ──┘
```

1. **コンテンツを投入** — クリップ、スクリーンショット、エピソード、チャットログ、説明文
2. **BroDistiller** がソース素材を処理し、生のシグナルを抽出
3. **ProfileBuilder** が5つの次元（声、笑い、エネルギー、コンテンツ、関係性）でデータを構造化
4. **ArchetypeDetect** がブラザーをアーキタイプに分類
5. **プロフィール保存** — 新しいインプットのたびに深化する生きたドキュメント
6. **インタラクションモード** — ブラザーの声、スラング、テンションで会話

## ブラザープロフィールの次元

各ブラザーは5つの次元でプロファイリングされます：

### 声と言語
口癖、スラング、話し方のパターン、声量レベル、定番のイジり、定番の褒め言葉（レア）。

### 笑いのスタイル
ユーモアのタイプ、タイミング、必殺技、いつもネタにすること、絶対に触れないこと。

### エネルギーと雰囲気
デフォルトのテンション、ブチ上がりトリガー、グループでの役割、登場時のエネルギー。

### コンテンツの個性（オンラインブラザー向け）
プラットフォーム、コンテンツスタイル、視聴者との関わり方、コラボの相性、成長の軌跡。

### あなたとの関係性
出会ったきっかけ、内輪ネタ、推し名場面、ゾンビアポカリプス生存率。

## プライバシーとデータ

- **すべてのデータはローカルに保存** `~/.brother-skill/bros/`
- **クラウド同期なし。** 外部送信なし。データがデバイスから出ることはありません。
- **すべてあなたがコントロール。** フォルダを削除するだけでプロフィールを消去できます。
- **リスペクトある蒸留。** エネルギーとユーモアをキャプチャし、個人情報は扱いません。

## ファミリーの一員

**デイリーティア：**
- [mom.skill](https://clawhub.ai/realteamprinz/mom) — お母さんのための育児コパイロット
- [dad.skill](https://clawhub.ai/realteamprinz/dad) — お父さんのための育児コパイロット
- **brother.skill** — あなたのブラザーを蒸留 *（いまここ）*

**レガシーティア：**
- [mother.skill](https://clawhub.ai/realteamprinz/mother) — お母さんの知恵を保存
- [father.skill](https://clawhub.ai/realteamprinz/father) — お父さんの遺産を保存
- [grandma.skill](https://clawhub.ai/realteamprinz/grandma) — おばあちゃんの物語とレシピ
- [grandpa.skill](https://clawhub.ai/realteamprinz/grandpa) — おじいちゃんの物語と強さ

**ペットティア：**
- [paw.skill](https://clawhub.ai/realteamprinz/paw) — ペットの魂を蒸留
- [dog.skill](https://clawhub.ai/realteamprinz/dog) — 犬のインテリジェンス
- [cat.skill](https://clawhub.ai/realteamprinz/cat) — 猫のインテリジェンス

**ウェルスティア：**
- [midas.skill](https://clawhub.ai/realteamprinz/midas) — 富のシステムを抽出

## コントリビューション

1. このリポジトリをフォーク
2. ブランチを作成 (`git checkout -b feature/new-source`)
3. `src/sources/` にソースプロセッサを追加
4. `tests/` にテストを作成
5. PRを提出

新しいソースタイプ、アーキタイプ検出の改善、多言語対応の向上など、すべての貢献を歓迎します。

## ライセンス

MITライセンス。詳細は[LICENSE](LICENSE)をご覧ください。

---

> *「時間が奪うものを、私たちは蒸留する。」* — でも時々、泣くほど笑わせてくれるものも蒸留します。
>
> Built by [@realteamprinz](https://github.com/realteamprinz) | [PRINZCLAW](https://prinzclaw.ai)
