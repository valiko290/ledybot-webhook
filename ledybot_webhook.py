from fastapi import FastAPI, Request
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler
import logging
import os

TOKEN = "8425735869:AAFtSQWIhhAMEIL2r053emBT_QLZN4jinjw"

app = FastAPI()
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot, None, workers=0)

logging.basicConfig(level=logging.INFO)


# === ОБРАБОТЧИК КОМАНД ===
def start(update, context):
    update.message.reply_text("Привет! Я LEDYBOT 🌸 — твоя быстрая, умная и надёжная помощница!")

dispatcher.add_handler(CommandHandler("start", start))


# === ХУК ДЛЯ ПОЛУЧЕНИЯ ОБНОВЛЕНИЙ ===
@app.post("/webhook/ledysecret123")
async def webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, bot)
    dispatcher.process_update(update)
    return {"ok": True}