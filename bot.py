import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is missing. Add it in Railway Variables.")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👟 Welcome!\n\n"
        "Here's what I can do:\n\n"
        "/latest — Latest updates\n"
        "/drops — Upcoming releases\n"
        "/restock — Restock alerts\n"
        "/sales — Deals & discounts\n"
        "/about — About this bot\n"
        "/contact — Send feedback"
    )


async def latest(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👟 Latest updates coming soon!")


async def drops(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📅 Upcoming drops coming soon!")


async def restock(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔁 Restock alerts coming soon!")


async def sales(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💸 Deals coming soon!")


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ℹ️ About this bot.")


async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📬 Send your feedback here.")


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("latest", latest))
    app.add_handler(CommandHandler("drops", drops))
    app.add_handler(CommandHandler("restock", restock))
    app.add_handler(CommandHandler("sales", sales))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("contact", contact))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
