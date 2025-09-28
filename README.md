# Chatbot Gemini Práctico

Proyecto de chatbot en consola que usa el modelo Gemini de Google para responder en español. Soporta roles como profesor, traductor, programador y asistente para adaptar las respuestas y ofrecer interacciones claras y útiles.

---

## Requisitos

- Python
- Clave API de Gemini
- Dependencias listadas en `requirements.txt`

---

## Instalación

## Clona el repositorio:

```bash
git clone https://github.com/sebagalde/chatbot-gemini-practico.git
cd chatbot-gemini-practico

## Crea un archivo .env en la raíz con las variables necesarias (ejemplo):

GEMINI_API_KEY=tu_api_key_aqui
MODEL=gemini-pro
MAX_RETRIES=3
TIMEOUT_SECONDS=30
MAX_HISTORY=12

## Instala las dependencias:

pip install -r requirements.txt

## Ejecuta el chatbot con:

python main.py

Al iniciar, selecciona un rol y luego podrás enviar mensajes para conversar con el bot.

Comandos disponibles

:rol profesor|traductor|programador|asistente — Cambia el rol del chatbot
:reset — Reinicia la conversación actual
:salir — Sale de la aplicación
:help — Muestra la ayuda con comandos disponibles