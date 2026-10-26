import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ====== НАСТРОЙКИ ======
BOT_TOKEN = "8986530501:AAGko7TT9u8yz8Ck82G--6Jag6XIxLHHYUI"
GROUP_ID = -5105416285  # ID твоей группы

START_MESSAGE = (
    "Привет! Сюда можно предложить новость.\n\n"
    "Отправь текст, фото, видео или документ — "
    "мы получим это и рассмотрим."
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(START_MESSAGE)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    message = update.message

    await context.bot.forward_message(
        chat_id=GROUP_ID,
        from_chat_id=message.chat_id,
        message_id=message.message_id
    )

    info = f"От: {user.full_name}"
    if user.username:
        info += f" (@{user.username})"
    await context.bot.send_message(chat_id=GROUP_ID, text=info)

    await message.reply_text("Спасибо! Новость отправлена.")

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, handle_message))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
