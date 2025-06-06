from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8199193176:AAF_2iUPwHHMSUjRdp40MOWPyabEYftOA0U"
GRUP_CHAT_ID = -1002327235209  # Grup chat ID'si buraya

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.video:
        await context.bot.forward_message(
            chat_id=GRUP_CHAT_ID,
            from_chat_id=update.message.chat_id,
            message_id=update.message.message_id
        )

app = ApplicationBuilder().token(BOT_TOKEN).build()

video_handler = MessageHandler(filters.VIDEO, handle_video)
app.add_handler(video_handler)

app.run_polling()
