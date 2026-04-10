<div align="center">

# brother.skill

> "Seu brother saiu do grupo, e agora ninguem lembra por que chamamos o Dave de 'O Incidente.'
> Seu streamer favorito foi banido, levando 3 anos de piadas internas junto.
> Seu amigo da internet sumiu, e o unico rastro e uma conta deletada no Discord.
> Transforme despedidas frias em Skills quentes — bem-vindo a brother-imortalidade!"

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Claude Code Skill](https://img.shields.io/badge/Claude_Code-Skill-orange.svg)](https://docs.anthropic.com)
[![AgentSkills Standard](https://img.shields.io/badge/AgentSkills-Standard-green.svg)](https://github.com/NousResearch/hermes-agent)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Ready-brightgreen.svg)](https://clawhub.ai/realteamprinz/brother)

[English](README.md) · [中文](README_CN.md) · [Español](README_ES.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · **Português**

</div>

---

**Destile seus brothers.** Aqueles que te fazem rir ate nao conseguir respirar. Online ou offline — se e seu brother, essa skill lembra de tudo.

Forneca materiais de origem (clipes do YouTube, videos do TikTok, streams da Twitch, logs do Discord, prints do WhatsApp, exports de grupo) mais suas proprias descricoes da pessoa, e receba uma **Skill de IA que realmente fala como eles**.

## Fontes Suportadas

| Fonte | Formato | O Que Captura |
|-------|---------|---------------|
| YouTube | URL do video ou transcricao | Estilo de fala, bordoes, energia, timing de humor |
| TikTok / Kwai | URL do video ou clipes salvos | Energia de video curto, momentos virais, bits recorrentes |
| Twitch | URLs de clips ou timestamps de VODs | Reacoes ao vivo, estilo de interacao com chat, momentos de rage |
| X / Twitter | URL do perfil ou export de tweets | Voz escrita, opinioes quentes, respostas de ratio |
| Discord | Export de logs de chat (.json) | Zoeira em tempo real, uso de memes, dinamica do grupo |
| WhatsApp | Export de conversa ou prints | Audios infinitos, stickers, figurinhas, memes brasileiros |
| Grupo (generico) | Export de texto de qualquer plataforma | Dinamica de grupo, piadas internas, papeis de cada um |
| Descricao Manual | Suas proprias palavras | Tudo que voce lembra — historias, impressoes, momentos |

## Instalacao

```bash
# OpenClaw
clawhub install realteamprinz/brother

# Hermes
hermes skills install brother-skill

# Claude Code
cp -r brother-skill/ ~/.claude/skills/

# Python (para o pipeline de destilacao)
git clone https://github.com/realteamprinz/brother-skill.git
cd brother-skill
pip install -r requirements.txt
```

## Inicio Rapido

### Destilar do YouTube

```bash
python distill.py --source youtube --url "https://youtube.com/watch?v=..." --name "Felipe Neto"
```

### Destilar de logs do Discord

```bash
python distill.py --source discord --file chat_export.json --name "Dave"
```

### Destilar do grupo de WhatsApp

```bash
python distill.py --source groupchat --file grupo_zap.txt --names "Mike,Dave,Jason"
```

### Destilar da sua propria descricao

```bash
python distill.py --source manual --name "Meu Brother Mike"
```

O modo interativo inicia — descreva seu brother e a skill constroi o perfil dele.

## Exemplos

### Felipe Neto

> "O que o Felipe Neto diria sobre eu ter perdido seguidores?"
>
> "GENTE. Para. PARA. Voce ta preocupado com SEGUIDOR? Eu ja perdi MILHOES de inscritos, ja tomei cancelamento de TUDO quanto e tipo, e to aqui firme e forte. Seguidor vai e vem. Conteudo bom FICA. Agora para de chorar e vai gravar um video."

### Cellbit

> "Me ajuda a resolver esse puzzle no jogo?"
>
> "Hmm... interessante. Olha, primeiro voce precisa prestar atencao nos detalhes. Sempre nos detalhes. Tem uma pista que voce ta ignorando, eu GARANTO. Volta la, olha de novo, e pensa: o que o desenvolvedor QUERIA que voce achasse? A resposta ta sempre escondida a vista."

### Casimiro

> "O que voce achou do jogo de ontem?"
>
> "IRMAO. QUE JOGO FOI ESSE CARA. Nao nao nao voce NAO entendeu. Aquele gol do segundo tempo — MISERICORDIA! Eu GRITEI aqui. Os vizinho bateram na parede. Eu to ROUCO. Melhor jogo do ano e nem acabou o campeonato ainda, ta MALUCO?"

### Alanzoka

> "To com raiva de um chefe no jogo, alguma dica?"
>
> "AAAAAAA MANO EU ODEIO ESSE CHEFE!! Ja morri umas 47 VEZES pra esse desgraca. Mas olha... calma... CALMA... voce tem que esquivar na hora certa e— NAO MANO MORRI DE NOVO!!! ISSO E IMPOSSIVEL!! ... ok respira... de novo... A GENTE VAI MATAR ESSE BOSS."

### Seu Grupo do Zap

> "Escreve nosso grupo planejando um churrasco"
>
> **Mike:** ae galera churrasco sabado quem vai
> **Dave:** depende, onde
> **Mike:** na casa do Jason logico
> **Jason:** ????? ninguem me perguntou
> **Mike:** jason tu tem a melhor churrasqueira
> **Jason:** [manda figurinha do gato com oculos]
> **Dave:** eu levo a carne mas alguem cobre a cerveja
> **Mike:** mano tu compra no atacadao fica barato
> **Dave:** entao vai la TU comprar
> **Jason:** [manda audio de 3 minutos que ninguem vai ouvir]

## Arquetipos de Brother

brother.skill reconhece diferentes tipos de brother:

| Arquetipo | Descricao | Exemplo Famoso |
|---|---|---|
| **O Hypador** | Energia maxima, sempre gritando, transforma tudo em evento | Casimiro |
| **O Zoeiro** | Insultos cirurgicamente precisos com cara de paisagem | KSI |
| **O Brother Suave** | Energia chill, fala pouco, mas quando fala — todo mundo para pra ouvir | Keanu Reeves |
| **O Agente do Caos** | Faz coisas que ninguem pediu, de alguma forma funciona | Alanzoka |
| **O Estrategista** | Transforma tudo em plano de negocios ou licao de vida | Felipe Neto |
| **O Matador Silencioso** | Fica 20 minutos quieto e solta uma frase que destroi todo mundo | Aquele amigo. Voce sabe quem. |
| **O Senhor dos Memes** | Se comunica exclusivamente por memes e figurinhas | Todo grupo tem um |
| **O Contador de Historias** | Toda experiencia vira uma recontagem dramatica de 10 minutos | Seu amigo mais engracado |

## Como Funciona

```
Material de Origem         Pipeline de Destilacao        Perfil do Brother
────────────────          ──────────────────────         ─────────────────
Clipes do YouTube  ──┐                                   ┌── Voz & Linguagem
Videos do TikTok   ──┤                                   ├── Estilo de Comedia
Streams da Twitch  ──┤    ┌─────────────────┐           ├── Energia & Vibe
Logs do Discord    ──┼──► │  BroDistiller   │ ────────► ├── Personalidade de Conteudo
Exports do WhatsApp──┤    │  ProfileBuilder │           ├── Papel no Grupo
Posts do Twitter   ──┤    │  ArchetypeDetect│           ├── Arquetipo
Grupos de chat     ──┤    └─────────────────┘           └── Relacionamento
Suas palavras      ──┘                                      + Modo de Interacao
```

1. **Alimente com conteudo** — clipes, prints, historias, logs de grupo, descricoes
2. **BroDistiller** processa o material de origem e extrai sinais brutos
3. **ProfileBuilder** estrutura os dados em cinco dimensoes (voz, comedia, energia, conteudo, relacionamento)
4. **ArchetypeDetect** classifica o brother em um dos 8 arquetipos
5. **Perfil salvo** — um documento vivo que se aprofunda com cada nova entrada
6. **Modo de Interacao** — converse com seu brother na voz dele, na giria dele, na energia dele

## Dimensoes do Perfil do Brother

Cada brother e perfilado em cinco dimensoes:

### Voz & Linguagem
Bordoes, girias, padroes de fala, nivel de volume, insultos favoritos, elogios favoritos (raros).

### Estilo de Comedia
Tipo de humor, timing, jogadas classicas, sobre o que sempre zoam, o que nunca tocam.

### Energia & Vibe
Nivel de energia padrao, gatilhos de pico, papel no grupo, energia de entrada.

### Personalidade de Conteudo (brothers online)
Plataforma, estilo de conteudo, interacao com audiencia, quimica de collab, como evoluiram.

### Relacionamento Com Voce
Como voce encontrou eles, piadas internas, momentos favoritos, nota de sobrevivencia no apocalipse zumbi.

## Privacidade e Dados

- **Todos os dados sao armazenados localmente** em `~/.brother-skill/bros/`
- **Sem sincronizacao na nuvem.** Sem transmissao externa. Zero dados saem do seu dispositivo.
- **Voce controla tudo.** Delete qualquer perfil de brother removendo a pasta dele.
- **Destilacao respeitosa.** Captura energia e humor, nao informacoes privadas.

## Parte da Familia

**Tier Diario:**
- [mom.skill](https://clawhub.ai/realteamprinz/mom) — Co-piloto parental para maes
- [dad.skill](https://clawhub.ai/realteamprinz/dad) — Co-piloto parental para pais
- **brother.skill** — Destile seus brothers *(voce esta aqui)*

**Tier Legado:**
- [mother.skill](https://clawhub.ai/realteamprinz/mother) — Preserve a sabedoria da sua mae
- [father.skill](https://clawhub.ai/realteamprinz/father) — Preserve o legado do seu pai
- [grandma.skill](https://clawhub.ai/realteamprinz/grandma) — As historias e receitas dela
- [grandpa.skill](https://clawhub.ai/realteamprinz/grandpa) — As historias e forca dele

**Tier Pet:**
- [paw.skill](https://clawhub.ai/realteamprinz/paw) — Destile a alma do seu pet
- [dog.skill](https://clawhub.ai/realteamprinz/dog) — Inteligencia canina
- [cat.skill](https://clawhub.ai/realteamprinz/cat) — Inteligencia felina

**Tier Riqueza:**
- [midas.skill](https://clawhub.ai/realteamprinz/midas) — Extraia sistemas de riqueza

## Contribuindo

1. Faca um fork deste repositorio
2. Crie sua branch (`git checkout -b feature/nova-fonte`)
3. Adicione seu processador de fonte em `src/sources/`
4. Escreva testes em `tests/`
5. Envie um PR

Novos tipos de fonte, melhor deteccao de arquetipos e melhorias multi-idioma sao todos bem-vindos.

## Licenca

Licenca MIT. Veja [LICENSE](LICENSE) para detalhes.

---

> *"Destilamos o que o tempo leva embora."* — Mas as vezes tambem destilamos o que nos faz rir ate chorar.
>
> Feito por [@realteamprinz](https://github.com/realteamprinz) | [PRINZCLAW](https://prinzclaw.ai)
