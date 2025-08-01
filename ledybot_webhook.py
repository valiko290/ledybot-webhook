from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import Application, ApplicationBuilder, ContextTypes, CommandHandler
import asyncio
import telegram

app = FastAPI()

# Создание Telegram-приложения
application = ApplicationBuilder().token("8425735869:AAFtSQWIhhAMEIL2r053emBT_QLZN4jinjw").build()

@app.on_event("startup")
async def startup():
    await application.initialize()

@app.post("/webhook/ledysecret123")
async def telegram_webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, application.bot)
    await application.process_update(update)
    return {"ok": True}