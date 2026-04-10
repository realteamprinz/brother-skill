<div align="center">

# brother.skill

> "형이 단톡방을 나갔는데, 이제 아무도 Dave를 왜 '그 사건'이라고 부르는지 기억 못 한다.
> 최애 스트리머가 밴 당해서 3년간의 밈이 같이 사라졌다.
> 인터넷 친구가 갑자기 사라지고, 남은 건 삭제된 디스코드 계정뿐.
> 차가운 작별을 따뜻한 Skill로 바꾸자 — 형제 불멸에 오신 걸 환영합니다!"

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Claude Code Skill](https://img.shields.io/badge/Claude_Code-Skill-orange.svg)](https://docs.anthropic.com)
[![AgentSkills Standard](https://img.shields.io/badge/AgentSkills-Standard-green.svg)](https://github.com/NousResearch/hermes-agent)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Ready-brightgreen.svg)](https://clawhub.ai/realteamprinz/brother)

[English](README.md) · [中文](README_CN.md) · [Español](README_ES.md) · [日本語](README_JA.md) · **한국어** · [Português](README_PT.md)

</div>

---

**형제를 증류하세요.** 숨 못 쉴 정도로 웃게 만드는 그 사람들. 온라인이든 오프라인이든 — 형제 같은 존재라면, 이 스킬이 모든 걸 기억합니다.

소스 자료(YouTube 클립, TikTok 영상, Twitch 스트림, Discord 로그, 카카오톡 스크린샷, 단톡방 내보내기)와 그 사람에 대한 본인의 설명을 제공하면, **진짜 그 사람처럼 말하는 AI Skill**을 얻을 수 있습니다.

## 지원 소스

| 소스 | 형식 | 캡처 내용 |
|------|------|-----------|
| YouTube | 영상 URL 또는 자막 | 말투, 유행어, 에너지, 유머 타이밍 |
| TikTok / Douyin | 영상 URL 또는 저장된 클립 | 숏폼 에너지, 바이럴 순간, 반복 비트 |
| Twitch | 클립 URL 또는 VOD 타임스탬프 | 실시간 리액션, 채팅 소통 스타일, 분노 순간 |
| 아프리카TV | 클립 URL 또는 VOD 타임스탬프 | BJ 방송 스타일, 별풍선 리액션, 팬 소통 |
| 카카오톡 | 스크린샷 또는 채팅 내보내기 | 한국식 인터넷 유머, 이모티콘, 카톡 말투 |
| 네이버 카페 | 게시글 또는 댓글 내보내기 | 커뮤니티 어투, 밈, 팬덤 문화 |
| X / Twitter | 프로필 URL 또는 트윗 내보내기 | 글쓰기 스타일, 뜨거운 의견, 비율 리플 |
| Discord | 채팅 로그 내보내기 (.json) | 실시간 입담, 밈 사용, 그룹 다이내믹스 |
| WeChat | 스크린샷 또는 채팅 내보내기 | 중국 인터넷 유머, 밈, 음성 메시지 스타일 |
| 단톡방 (일반) | 모든 플랫폼의 텍스트 내보내기 | 다인 관계, 인사이드 조크, 역할 |
| 직접 설명 | 본인의 말로 | 기억나는 모든 것 — 이야기, 인상, 순간들 |

## 설치

```bash
# OpenClaw
clawhub install realteamprinz/brother

# Hermes
hermes skills install brother-skill

# Claude Code
cp -r brother-skill/ ~/.claude/skills/

# Python (증류 파이프라인용)
git clone https://github.com/realteamprinz/brother-skill.git
cd brother-skill
pip install -r requirements.txt
```

## 빠른 시작

### YouTube에서 증류

```bash
python distill.py --source youtube --url "https://youtube.com/watch?v=..." --name "침착맨"
```

### Discord 로그에서 증류

```bash
python distill.py --source discord --file chat_export.json --name "Dave"
```

### 카카오톡 단톡방에서 증류

```bash
python distill.py --source groupchat --file kakaotalk_export.txt --names "민수,동혁,재원"
```

### 직접 설명으로 증류

```bash
python distill.py --source manual --name "우리 형 민수"
```

인터랙티브 모드가 시작됩니다 — 형제를 설명하면 스킬이 프로필을 빌드합니다.

## 예시

### 침착맨

> "침착맨한테 오늘 하루 망했다고 말하면?"
>
> "아... 하루 망했어요? 그거 참... 근데 하루가 망한 건지 원래 그런 건지 잘 구분을 해야 해요. 제 경우에는 매일이 좀 그래서 기준이 없거든요. 침착하게 갑시다."

### 우왁굳

> "우왁굳한테 새 게임 추천해달라고 하면?"
>
> "게임? 게임을 왜 추천을 받아! 그냥 이상한 거 하나 틀어놓고 채팅이 미쳐 돌아가게 만들면 그게 명작이야!! 아 진짜 왜 이렇게 재밌어 하하하하하"

### 이말년

> "이말년한테 오늘 있었던 일 말하면?"
>
> "야 잠깐만, 이거 만화로 그려야 해. 진짜 이건 네컷 감이야. 첫 번째 컷에 네가 등장하고... 아 잠깐 눈을 좀 크게 그려야 공포감이 살지."

### MrBeast

> "조회수 어떻게 올려요?"
>
> "썸네일 바꿔. 아니 진짜로. 1만 달러 나눠주기 해봤어? 그건 보통 효과 있어. 그리고 제목은 사람들이 반드시 클릭하고 싶게 만들어야 해."

### 단톡방

> "우리 단톡방에서 여행 계획 세우는 거 써줘"
>
> **민수:** 야 이번 주말 여행 갈 사람
> **동혁:** 어디
> **민수:** 몰라 어디 좋은 데
> **동혁:** 그건 계획이 아니잖아
> **재원:** [짤 전송]
> **민수:** 재원아 갈 거야 말 거야
> **재원:** [짤 하나 더 전송]
> **동혁:** 내가 운전할 테니까 누가 기름값 내
> **민수:** 야 너 테슬라잖아
> **동혁:** 그래서. 누가 충전비 내냐고

## 형제 아키타입

brother.skill은 다양한 형제 유형을 인식합니다:

| 아키타입 | 설명 | 유명한 예시 |
|----------|------|-------------|
| **하이프맨** | 최대 에너지, 항상 소리 지름, 모든 걸 이벤트로 만듦 | IShowSpeed |
| **디스 장인** | 수술처럼 정확한 디스를 무표정으로 날림 | 침착맨, KSI |
| **쿨한 형** | 차분한 에너지, 말수 적음, 하지만 한 마디 하면 — 다 경청 | Keanu Reeves |
| **카오스 에이전트** | 아무도 안 시킨 걸 하는데, 어째 잘 됨 | 우왁굳, Jake Paul |
| **전략 형** | 모든 걸 사업 계획이나 인생 조언으로 바꿈 | MrBeast |
| **사일런트 킬러** | 20분 동안 조용하다가 한 마디로 전원 사살 | 그 친구. 누군지 알잖아. |
| **밈 군주** | 밈과 리액션 이미지로만 소통 | 모든 단톡방에 한 명씩 있음 |
| **이야기꾼** | 모든 경험을 10분짜리 드라마틱 리텔링으로 바꿈 | 이말년, 제일 웃긴 친구 |

## 작동 원리

```
소스 자료                  증류 파이프라인                   형제 프로필
────────                ──────────────────                ──────────
YouTube 클립       ──┐                                    ┌── 말투 & 언어
TikTok 영상        ──┤                                    ├── 코미디 스타일
Twitch 스트림      ──┤    ┌─────────────────┐            ├── 에너지 & 바이브
아프리카TV 클립    ──┤    │  BroDistiller   │            ├── 콘텐츠 개성
Discord 로그       ──┼──► │  ProfileBuilder │ ────────►  ├── 그룹 역할
카카오톡 내보내기  ──┤    │  ArchetypeDetect│            ├── 아키타입
네이버 카페 글     ──┤    └─────────────────┘            └── 관계
Twitter 게시글     ──┤                                       + 인터랙션 모드
단톡방             ──┤
당신의 말          ──┘
```

1. **콘텐츠 입력** — 클립, 스크린샷, 이야기, 단톡방 로그, 설명
2. **BroDistiller**가 소스 자료를 처리하고 원시 신호를 추출
3. **ProfileBuilder**가 데이터를 5개 차원(말투, 코미디, 에너지, 콘텐츠, 관계)으로 구조화
4. **ArchetypeDetect**가 형제를 8개 아키타입 중 하나로 분류
5. **프로필 저장** — 새로운 입력마다 깊어지는 살아있는 문서
6. **인터랙션 모드** — 형제의 목소리, 슬랭, 에너지로 대화

## 형제 프로필 차원

각 형제는 5개 차원으로 프로파일링됩니다:

### 말투 & 언어
유행어, 슬랭, 말버릇, 볼륨 레벨, 자주 쓰는 디스, 자주 쓰는 칭찬 (드물게).

### 코미디 스타일
유머 유형, 타이밍, 시그니처 무브, 항상 농담하는 주제, 절대 건드리지 않는 주제.

### 에너지 & 바이브
기본 에너지 레벨, 피크 트리거, 그룹 역할, 등장 에너지.

### 콘텐츠 개성 (온라인 형제)
플랫폼, 콘텐츠 스타일, 시청자 인터랙션, 콜라보 케미, 어떻게 변해왔는지.

### 당신과의 관계
어떻게 알게 됐는지, 인사이드 조크, 최고의 순간, 좀비 아포칼립스 생존 등급.

## 개인정보 및 데이터

- **모든 데이터는 로컬에 저장** `~/.brother-skill/bros/`
- **클라우드 동기화 없음.** 외부 전송 없음. 데이터가 기기를 떠나지 않습니다.
- **모든 것을 당신이 제어합니다.** 폴더를 삭제하면 프로필이 제거됩니다.
- **존중하는 증류.** 에너지와 유머를 캡처하고, 개인 정보는 다루지 않습니다.

## 패밀리의 일원

**데일리 티어:**
- [mom.skill](https://clawhub.ai/realteamprinz/mom) — 엄마를 위한 육아 코파일럿
- [dad.skill](https://clawhub.ai/realteamprinz/dad) — 아빠를 위한 육아 코파일럿
- **brother.skill** — 형제를 증류하세요 *(지금 여기)*

**레거시 티어:**
- [mother.skill](https://clawhub.ai/realteamprinz/mother) — 어머니의 지혜를 보존하세요
- [father.skill](https://clawhub.ai/realteamprinz/father) — 아버지의 유산을 보존하세요
- [grandma.skill](https://clawhub.ai/realteamprinz/grandma) — 할머니의 이야기와 레시피
- [grandpa.skill](https://clawhub.ai/realteamprinz/grandpa) — 할아버지의 이야기와 강인함

**펫 티어:**
- [paw.skill](https://clawhub.ai/realteamprinz/paw) — 반려동물의 영혼을 증류하세요
- [dog.skill](https://clawhub.ai/realteamprinz/dog) — 반려견 인텔리전스
- [cat.skill](https://clawhub.ai/realteamprinz/cat) — 반려묘 인텔리전스

**웰스 티어:**
- [midas.skill](https://clawhub.ai/realteamprinz/midas) — 부의 시스템 추출

## 기여하기

1. 이 레포를 포크하세요
2. 브랜치를 만드세요 (`git checkout -b feature/new-source`)
3. `src/sources/`에 소스 프로세서를 추가하세요
4. `tests/`에 테스트를 작성하세요
5. PR을 제출하세요

새로운 소스 타입, 더 나은 아키타입 감지, 다국어 개선 모두 환영합니다.

## 라이선스

MIT 라이선스. 자세한 내용은 [LICENSE](LICENSE)를 확인하세요.

---

> *"시간이 가져가는 것을 우리가 증류합니다."* — 하지만 때로는 울면서 웃게 만드는 것도 증류합니다.
>
> Built by [@realteamprinz](https://github.com/realteamprinz) | [PRINZCLAW](https://prinzclaw.ai)
