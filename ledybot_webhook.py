"
Основной скрипт Telegram-бота на FastAPI + Webhook.
"
from fastapi import FastAPI, Request
import telegram
import asyncio
import os

BOT_TOKEN = "8425735869:AAFtSQWIhhAMEIL2r053emBT_QLZN4jinjw"
SECRET_TOKEN = "ledysecret12"

bot = telegram.Bot(token=BOT_TOKEN)
app = FastAPI()

@app.post(f"/webhook/{SECRET_TOKEN}")
async def webhook(request: Request):
    data = await request.json()
    update = telegram.Update.de_json(data, bot)
    if update.message:
        chat_id = update.message.chat.id
        await bot.send_message(chat_id=chat_id, text="🌸 Привет! Я LEDYBOT — твоя умная помощница!")
    return "ok"
