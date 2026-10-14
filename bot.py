import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is missing. Add it in Railway Variables.")


# ============================================
# KEYBOARD MENU
# ============================================

MENU = ReplyKeyboardMarkup(
    [
        ["👟 New Drops", "🔥 Promos"],
        ["🔁 Restocks", "📏 Size Guide"],
        ["ℹ️ About", "📬 Contact"]
    ],
    resize_keyboard=True
)


# ============================================
# COMMAND HANDLERS
# ============================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👟 Welcome to Melhores!\n\n"
        "Your daily source for the best female sneaker promos, "
        "new drops, restocks, and trending styles — all inside Telegram.\n\n"
        "Tap a button below or use the commands to get started.",
        reply_markup=MENU
    )


async def new_drops(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👟 NEW DROPS\n\n"
        "Fresh sneaker releases for women will appear here.\n"
        "Check back daily for updates!"
    )


async def promos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 PROMOS & DEALS\n\n"
        "Current sneaker sales and discounts will appear here.\n"
        "Stay tuned!"
    )


async def restocks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔁 RESTOCK ALERTS\n\n"
        "Restocked sneakers will be listed here.\n"
        "We'll notify you when popular pairs are back!"
    )


async def size_guide(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📏 WOMEN'S SNEAKER SIZE GUIDE\n\n"
        "US 5  = EU 35.5 = UK 3\n"
        "US 6  = EU 36.5 = UK 4\n"
        "US 7  = EU 38   = UK 5\n"
        "US 8  = EU 39   = UK 6\n"
        "US 9  = EU 40.5 = UK 7\n"
        "US 10 = EU 42   = UK 8\n\n"
        "Tip: Sneakers usually fit true to size. "
        "Go half a size up for narrow feet."
    )


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ ABOUT MELHORES\n\n"
        "Melhores is your daily source for the best female sneaker "
        "promos, new drops, restocks, and trending styles — all inside Telegram.\n\n"
        "No external links. No spam. Just clean sneaker deals for women. 👟"
    )


async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📬 CONTACT & FEEDBACK\n\n"
        "Have a question or want to request a sneaker update?\n"
        "Send your message here and we'll get back to you."
    )


# ============================================
# BUTTON HANDLER
# ============================================

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "👟 New Drops":
        await new_drops(update, context)
    elif text == "🔥 Promos":
        await promos(update, context)
    elif text == "🔁 Restocks":
        await restocks(update, context)
    elif text == "📏 Size Guide":
        await size_guide(update, context)
    elif text == "ℹ️ About":
        await about(update, context)
    elif text == "📬 Contact":
        await contact(update, context)
    else:
        await update.message.reply_text(
            "Please tap a button below or use a command.",
            reply_markup=MENU
        )


# ============================================
# MAIN
# ============================================

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("newdrops", new_drops))
    app.add_handler(CommandHandler("promos", promos))
    app.add_handler(CommandHandler("restocks", restocks))
    app.add_handler(CommandHandler("size", size_guide))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("contact", contact))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, button_handler))

    print("Melhores bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
