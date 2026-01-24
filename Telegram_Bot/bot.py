
# telegram_bot/bot.py

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

from config import BOT_TOKEN


# Handler untuk /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo! 👋\n\n"
        "Saya adalah sistem diagnosis berbasis gejala.\n"
        "Silakan pilih gejala untuk memulai."
    )


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Daftarkan command
    app.add_handler(CommandHandler("start", start))

    print("🤖 Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
