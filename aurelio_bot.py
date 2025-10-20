# aurelio_bot_pedidos.py

from dotenv import load_dotenv
import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ContextTypes, filters
)

# ----------------------------
# Cargar el .env
# ----------------------------
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TELEGRAM_TOKEN:
    print("❌ No se encontró TELEGRAM_TOKEN. Revisa tu archivo .env")
    exit(1)

# ----------------------------
# Productos disponibles
# ----------------------------
productos = ["Café 250g ☕", "Café 500g ☕", "Pan artesanal 🍞", "Miel orgánica 🍯"]

# ----------------------------
# Comandos del bot
# ----------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /start"""
    menu = ReplyKeyboardMarkup.from_column(productos, resize_keyboard=True)
    await update.message.reply_text(
        "¡Hola! Soy *Aurelio Bot* 🤖\nElige el producto que te interesa:",
        parse_mode="Markdown",
        reply_markup=menu
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /help"""
    help_text = (
        "Comandos disponibles:\n"
        "/start - Iniciar pedido\n"
        "/help - Mostrar ayuda\n"
        "/info - Información del bot"
    )
    await update.message.reply_text(help_text)

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /info"""
    await update.message.reply_text("Aurelio Bot v1.1\nCreado por Isela L. 😎\nListo para tomar pedidos 🛍️")

# ----------------------------
# Mensajes del usuario (flujo del pedido)
# ----------------------------
async def manejar_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text
    user_data = context.user_data

    # Si el usuario elige un producto del menú
    if texto in productos:
        user_data["producto"] = texto
        await update.message.reply_text(
            f"Has elegido *{texto}* 🛒\n¿Cuántas unidades deseas?",
            parse_mode="Markdown"
        )

    # Si el usuario ya eligió producto y ahora indica cantidad
    elif texto.isdigit() and "producto" in user_data:
        cantidad = int(texto)
        producto = user_data["producto"]
        await update.message.reply_text(
            f"✅ Pedido registrado:\n\n*{producto}* x {cantidad} unidades\n\nGracias por tu compra 💕✨",
            parse_mode="Markdown"
        )
        user_data.clear()  # Limpiamos el contexto del usuario

    else:
        await update.message.reply_text("No entendí 😅. Escribe /start para ver el menú de productos.")

# ----------------------------
# Configuración del bot
# ----------------------------
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

# Handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("info", info))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_mensaje))

# ----------------------------
# Ejecutar el bot
# ----------------------------
print("🤖 Bot de Aurelio iniciado correctamente... ✅")
app.run_polling()
