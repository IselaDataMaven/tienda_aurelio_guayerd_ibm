# 🤖 Aurelio Bot

<img width="1536" height="1024" alt="ChatGPT Image 20 oct 2025, 12_55_31 p m" src="https://github.com/user-attachments/assets/a7618d0b-3c12-4684-baec-b95e3343af6d" />

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" />
  <img src="https://img.shields.io/badge/Telegram%20Bot-API-26A5E4?logo=telegram&logoColor=white" />
  <img src="https://img.shields.io/badge/asyncio-powered-ff69b4" />
  <img src="https://img.shields.io/badge/license-MIT-green" />
</p>

---

## 🛍️ Descripción

**Aurelio Bot** es un asistente creado para automatizar pedidos de productos directamente desde **Telegram**.  
Permite al usuario seleccionar artículos, indicar cantidades y recibir una confirmación inmediata del pedido —todo sin salir del chat.

> 💬 Ideal para pequeñas tiendas, cafeterías o emprendimientos que buscan una forma práctica y moderna de recibir pedidos.

---

## ⚙️ Tecnologías usadas

| Tecnología | Descripción |
|-------------|--------------|
| 🐍 **Python 3.10+** | Lenguaje base del proyecto |
| 💬 **python-telegram-bot (v20+)** | Librería para interactuar con la API de Telegram |
| 🌱 **dotenv** | Carga de variables de entorno de forma segura |
| 🧠 **async/await** | Manejo de eventos asíncronos para respuestas rápidas |

---

## 🚀 Instalación y ejecución

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/tuusuario/aurelio-bot.git
cd aurelio-bot

2.CREAR UN ENTORNO VIRTUAL
python -m venv venv
source venv/bin/activate   # En Linux / Mac
venv\Scripts\activate      # En Windows

3.INSTALAR DEPENDENCIAS
pip install -r requirements.txt

4.CONFIGURAR EL ARCHIVO .env
TELEGRAM_TOKEN=tu_token_aqui

💬 Uso del bot

Ejecuta el bot con:

python aurelio_bot_pedidos.py

Abre Telegram y busca tu bot (por su nombre o usuario).

Escribe /start para iniciar la conversación.

Elige un producto → Indica la cantidad → Recibe la confirmación ✅

Ejemplo de conversación:

Usuario: /start
Bot: ¡Hola! Soy Aurelio Bot 🤖
Bot: Elige el producto que te interesa
Usuario: Café 250g ☕
Bot: Has elegido Café 250g ☕ ¿Cuántas unidades deseas?
Usuario: 2
Bot: ✅ Pedido registrado: Café 250g x 2 unidades. ¡Gracias por tu compra!

📁 Estructura del proyecto
aurelio-bot/
│
├── aurelio_bot_pedidos.py     # Código principal del bot
├── .env                       # Token del bot (no subir a GitHub)
├── requirements.txt            # Dependencias del proyecto
└── README.md                   # Documentación (este archivo)
🧩 Requisitos

Python 3.10 o superior

Una cuenta de Telegram

Token generado por @BotFather

💡 Mejoras futuras

💾 Guardar pedidos en una base de datos (SQLite o Firebase)

💬 Enviar notificaciones a Aurelio cuando haya un nuevo pedido

📸 Agregar imágenes o precios de los productos

🧾 Generar un resumen de ventas automático

🧑‍💻 Autora

Isela L.
✨ Project Manager & AI Enthusiast
📍 México

💌 LinkedIn https://www.linkedin.com/in/iseladatamaven/
 | GitHub    https://github.com/IselaDataMaven


<p align="center">Hecho con 💕 y ☕ por Isela</p> ```
💡 Recomendaciones para tu GitHub:



En requirements.txt, incluye:

python-telegram-bot==20.6
python-dotenv



