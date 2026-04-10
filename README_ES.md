<div align="center">

# brother.skill

> "Tu hermano se salio del grupo, y ahora nadie recuerda por que le decimos a Dave 'El Incidente.'
> Tu streamer favorito fue baneado, llevandose 3 anos de chistes internos.
> Tu amigo de internet desaparecio, y lo unico que queda es una cuenta de Discord eliminada.
> Convierte las despedidas frias en Skills calidos -- bienvenido a la hermano-inmortalidad!"

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Claude Code Skill](https://img.shields.io/badge/Claude_Code-Skill-orange.svg)](https://docs.anthropic.com)
[![AgentSkills Standard](https://img.shields.io/badge/AgentSkills-Standard-green.svg)](https://github.com/NousResearch/hermes-agent)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Ready-brightgreen.svg)](https://clawhub.ai/realteamprinz/brother)

[English](README.md) | [中文](README_CN.md) | [日本語](README_JA.md) | [한국어](README_KO.md) | [Português](README_PT.md)

</div>

---

**Destila a tus hermanos.** Los que te hacen reir hasta que no puedes respirar. Online u offline -- si es tu hermano, este skill lo recuerda todo.

Proporciona materiales de origen (clips de YouTube, videos de TikTok, streams de Twitch, logs de Discord, capturas de WhatsApp, capturas de WeChat, exportaciones de chats grupales) mas tus propias descripciones de la persona, y obtendras un **AI Skill que realmente habla como ellos**.

## Fuentes Soportadas

| Fuente | Formato | Lo Que Captura |
|--------|---------|----------------|
| YouTube | URL de video o transcripcion | Estilo de habla, muletillas, energia, timing de humor |
| TikTok / Douyin | URL de video o clips guardados | Energia de formato corto, momentos virales, bits recurrentes |
| Twitch | URLs de clips o timestamps de VODs | Reacciones en vivo, estilo de interaccion con el chat, momentos de rabia |
| X / Twitter | URL de perfil o exportaciones de tweets | Voz escrita, opiniones picantes, respuestas de ratio |
| Discord | Exportacion de chat (.json) | Bantereo en tiempo real, uso de memes, dinamicas de grupo |
| WhatsApp | Exportacion de chat (.txt) o capturas | Humor latino, audios iconicos, stickers, dinamica de grupo |
| WeChat | Captura de pantalla o exportacion de chat | Humor de internet chino, memes, estilo de mensajes de voz |
| Chat Grupal (generico) | Exportacion de texto de cualquier plataforma | Dinamicas multi-persona, chistes internos, roles |
| Descripcion Manual | Tus propias palabras | Todo lo que recuerdes -- historias, impresiones, momentos |

## Instalacion

```bash
# OpenClaw
clawhub install realteamprinz/brother

# Hermes
hermes skills install brother-skill

# Claude Code
cp -r brother-skill/ ~/.claude/skills/

# Python (para el pipeline de destilacion)
git clone https://github.com/realteamprinz/brother-skill.git
cd brother-skill
pip install -r requirements.txt
```

## Inicio Rapido

### Destilar desde YouTube

```bash
python distill.py --source youtube --url "https://youtube.com/watch?v=..." --name "Ibai"
```

### Destilar desde logs de Discord

```bash
python distill.py --source discord --file chat_export.json --name "Dave"
```

### Destilar desde WhatsApp

```bash
python distill.py --source whatsapp --file chat_whatsapp.txt --name "El Grupo de los Pibes"
```

### Destilar desde chat grupal

```bash
python distill.py --source groupchat --file groupchat.txt --names "Mike,Dave,Jason"
```

### Destilar desde tu propia descripcion

```bash
python distill.py --source manual --name "Mi Hermano Mike"
```

Se inicia el modo interactivo -- describe a tu hermano y el skill construye su perfil.

## Ejemplos

### Ibai

> "Que diria Ibai sobre mi mal dia?"
>
> "PERO TU ESTAS LOCO?! MAL DIA?! QUE ME ESTAS CONTANDOOO! Mira, ven aqui, nos hacemos un stream de cocina, nos comemos un chuleton de tres kilos y me cuentas tus problemas mientras yo GRITO a la sarten. MAL DIA DICE. AQUI NO HAY DIAS MALOS, AQUI HAY CHULETONES."

### ElRubius

> "Deberia empezar a stremear?"
>
> "Tio, yo empece haciendo videos en mi habitacion con un micro de cinco euros y mira... bueno, ahora sigo en una habitacion pero mas grande. Hazlo, empieza, da igual si al principio es un desastre. Los primeros videos de todos son un cringe absoluto. Los mios? Ni te cuento. Pero ahi esta la magia, chaval."

### MrBeast

> "Como consigo mas vistas?"
>
> "Cambia tu thumbnail. No, en serio. Has intentado regalar $10,000? Eso suele funcionar. Ademas tu titulo tiene que hacer que la gente NECESITE hacer clic."

### Luisito Comunica

> "Que hago si me aburro en casa?"
>
> "Mira, te voy a contar algo. Una vez estaba en un pueblito en medio de la nada en Oaxaca, sin internet, sin nada, y termine en una fiesta patronal bailando con una senora de 80 anos que me enseno a hacer mole. MOLE, wey. La aventura no esta en el destino, esta en decir que si a todo. Sal de tu casa. O mejor, ve a la cocina y haz un mole."

### Auronplay

> "Mi companero de piso no limpia nunca"
>
> "A ver. Que no limpia. Vale. Pregunta seria: tu companero de piso es una persona o un mapache? Porque los mapaches al menos tienen la excusa de ser animales. Tu companero simplemente ha decidido que vivir en la mugre es un estilo de vida. Respetable? No. Sorprendente? Tampoco."

### Jake Paul

> "Que diria Jake Paul sobre mi mal dia?"
>
> "BRO. MAL DIA? No TENEMOS dias malos. Sabes que hacemos? Compramos un Lamborghini y ATROPELLAMOS al mal dia. IT'S EVERYDAY BRO."

### Tu Chat Grupal

> "Escribe nuestro chat grupal planeando un viaje"
>
> **Mike:** ey viaje este finde quien se apunta
> **Dave:** depende a donde
> **Mike:** nose a algun lado chido
> **Dave:** eso no es un plan
> **Jason:** [envia meme]
> **Mike:** jason vas o no
> **Jason:** [envia otro meme]
> **Dave:** yo manejo pero alguien pone la gasolina
> **Mike:** bro tu manejas un Tesla
> **Dave:** exacto. Alguien paga la carga

## Arquetipos de Hermano

brother.skill reconoce diferentes tipos de hermano:

| Arquetipo | Descripcion | Ejemplo Famoso |
|---|---|---|
| **El Hype Man** | Energia al maximo, siempre gritando, convierte todo en un evento | IShowSpeed |
| **El Roast Master** | Insultos quirurgicamente precisos con cara de poker | Auronplay |
| **El Hermano Tranqui** | Energia chill, habla poco, pero cuando habla -- todos escuchan | Keanu Reeves |
| **El Agente del Caos** | Hace cosas que nadie pidio, y de alguna forma funciona | Jake Paul |
| **El Hermano Estratega** | Convierte todo en un plan de negocios o leccion de vida | MrBeast |
| **El Asesino Silencioso** | Callado 20 minutos, luego suelta una frase que destruye a todos | Ese amigo. Tu sabes quien. |
| **El Senor de los Memes** | Se comunica exclusivamente con memes e imagenes de reaccion | Todos los grupos tienen uno |
| **El Cuentacuentos** | Cada experiencia se convierte en una historia dramatica de 10 minutos | Luisito Comunica |

## Como Funciona

```
Material de Origen          Pipeline de Destilacion         Perfil de Hermano
────────────────          ─────────────────────────         ─────────────────
Clips de YouTube   ──┐                                     ┌── Voz y Lenguaje
Videos de TikTok   ──┤                                     ├── Estilo de Comedia
Streams de Twitch  ──┤    ┌──────────────────────┐         ├── Energia y Vibra
Logs de Discord    ──┼──► │  BroDistiller        │ ──────► ├── Personalidad de Contenido
Chats de WhatsApp  ──┤    │  ProfileBuilder      │         ├── Rol en el Grupo
Exports de WeChat  ──┤    │  ArchetypeDetect     │         ├── Arquetipo
Posts de Twitter   ──┤    └──────────────────────┘         └── Relacion
Chats grupales     ──┤                                        + Modo de Interaccion
Tus palabras       ──┘
```

1. **Alimentalo con contenido** -- clips, capturas, historias, logs de chats grupales, descripciones
2. **BroDistiller** procesa el material de origen y extrae senales crudas
3. **ProfileBuilder** estructura los datos en cinco dimensiones (voz, comedia, energia, contenido, relacion)
4. **ArchetypeDetect** clasifica al hermano en uno de 8 arquetipos
5. **Perfil guardado** -- un documento vivo que se profundiza con cada nuevo input
6. **Modo de Interaccion** -- habla con tu hermano en su voz, su jerga, su energia

## Dimensiones del Perfil de Hermano

Cada hermano se perfila en cinco dimensiones:

### Voz y Lenguaje
Muletillas, jerga, patrones de habla, nivel de volumen, insultos favoritos, cumplidos favoritos (raros).

### Estilo de Comedia
Tipo de humor, timing, movimientos firma, de que siempre bromean, lo que nunca tocan.

### Energia y Vibra
Nivel de energia por defecto, triggers de pico, rol en el grupo, energia de entrada.

### Personalidad de Contenido (hermanos online)
Plataforma, estilo de contenido, interaccion con audiencia, quimica de colaboracion, como han evolucionado.

### Relacion Contigo
Como los encontraste, chistes internos, momentos favoritos, calificacion de supervivencia en apocalipsis zombie.

## Privacidad y Datos

- **Todos los datos se almacenan localmente** en `~/.brother-skill/bros/`
- **Sin sincronizacion en la nube.** Sin transmision externa. Cero datos salen de tu dispositivo.
- **Tu controlas todo.** Elimina cualquier perfil de hermano borrando su carpeta.
- **Destilacion respetuosa.** Captura energia y humor, no informacion privada.

## Parte de la Familia

**Nivel diario:**
- [mom.skill](https://clawhub.ai/realteamprinz/mom) -- Copiloto de crianza para madres
- [dad.skill](https://clawhub.ai/realteamprinz/dad) -- Copiloto de crianza para padres
- **brother.skill** -- Destila a tus hermanos *(estas aqui)*

**Nivel legado:**
- [mother.skill](https://clawhub.ai/realteamprinz/mother) -- Preserva la sabiduria de tu madre
- [father.skill](https://clawhub.ai/realteamprinz/father) -- Preserva el legado de tu padre
- [grandma.skill](https://clawhub.ai/realteamprinz/grandma) -- Sus historias y recetas
- [grandpa.skill](https://clawhub.ai/realteamprinz/grandpa) -- Sus historias y fortaleza

**Nivel mascotas:**
- [paw.skill](https://clawhub.ai/realteamprinz/paw) -- Destila el alma de tu mascota
- [dog.skill](https://clawhub.ai/realteamprinz/dog) -- Inteligencia canina
- [cat.skill](https://clawhub.ai/realteamprinz/cat) -- Inteligencia felina

**Nivel riqueza:**
- [midas.skill](https://clawhub.ai/realteamprinz/midas) -- Extrae sistemas de riqueza

## Contribuir

1. Haz fork de este repositorio
2. Crea tu rama (`git checkout -b feature/nueva-fuente`)
3. Agrega tu procesador de fuente en `src/sources/`
4. Escribe tests en `tests/`
5. Envia un PR

Nuevos tipos de fuente, mejor deteccion de arquetipos y mejoras multi-idioma son bienvenidos.

## Licencia

Licencia MIT. Consulta [LICENSE](LICENSE) para mas detalles.

---

> *"Destilamos lo que el tiempo se lleva."* -- Pero a veces tambien destilamos lo que nos hace reir hasta llorar.
>
> Creado por [@realteamprinz](https://github.com/realteamprinz) | [PRINZCLAW](https://prinzclaw.ai)
