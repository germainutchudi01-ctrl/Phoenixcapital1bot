from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "METS_ICI_LE_TOKEN_DE_BOTFATHER"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📊 Signaux Trading"],
        ["🎁 Bonus Premier Dépôt"],
        ["👥 Parrainage"],
        ["🌍 Langues"],
        ["📞 Support"]
    ]

    await update.message.reply_text(
        "🦅 Bienvenue sur PHOENIX CAPITAL\n\n"
        "Votre partenaire pour une expérience de trading structurée.\n\n"
        "Choisissez une option :",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

async def messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📊 Signaux Trading":
        await update.message.reply_text(
            "Les signaux de trading sont publiés dans le canal officiel Phoenix Capital."
        )

    elif text == "🎁 Bonus Premier Dépôt":
        await update.message.reply_text(
            "Recevez votre bonus selon le montant de votre premier dépôt."
        )

    elif text == "👥 Parrainage":
        await update.message.reply_text(
            "Invitez vos amis et obtenez vos récompenses de parrainage."
        )

    elif text == "🌍 Langues":
        await update.message.reply_text(
            "Français 🇫🇷\nEnglish 🇬🇧\nالعربية 🇸🇦"
        )

    elif text == "📞 Support":
        await update.message.reply_text(
            "@PhoenixCapitalSupport"
        )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, messages))

print("Bot Phoenix Capital démarré...")

app.run_polling()