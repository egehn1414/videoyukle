from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
TARGET_CHAT_ID = os.getenv("TARGET_CHAT_ID")

async def handle_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message

    if message:
        caption = message.caption or ""

        if message.photo:
            # En büyük çözünürlükteki fotoğrafı al
            photo = message.photo[-1]
            await context.bot.send_photo(
                chat_id=TARGET_CHAT_ID,
                photo=photo.file_id,
                caption=caption
            )

        elif message.video:
            await context.bot.send_video(
                chat_id=TARGET_CHAT_ID,
                video=message.video.file_id,
                caption=caption
            )

app = ApplicationBuilder().token(BOT_TOKEN).build()

media_handler = MessageHandler(filters.PHOTO | filters.VIDEO, handle_media)
app.add_handler(media_handler)

app.run_polling()
