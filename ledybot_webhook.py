# ledybot_webhook.py
from fastapi import FastAPI, Request, HTTPException
import httpx
import os
import asyncio

app = FastAPI()

BOT_TOKEN = os.getenv("BOT_TOKEN")
BASE_URL = os.getenv("BASE_URL")
SECRET_TOKEN = os.getenv("SECRET_TOKEN") or "supersecret"

TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.post(f"/telegram/{{token}}")
async def telegram_webhook(token: str, request: Request):
    if token != SECRET_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid secret token")

    payload = await request.json()
    message = payload.get("message") or payload.get("edited_message")

    if message:
        chat_id = message["chat"]["id"]
        text = message.get("text", "")

        if text == "/start":
            reply = "Привет! Я LEDYBOT 🌸 — твоя быстрая, умная и нежная помощница! Напиши, что тебе нужно, и я всё подберу сама, легко и красиво! 😉"
        else:
            reply = f"🔎 Сейчас ищу: «{text}»... (скоро буду искать по-настоящему!) 🚀"

        await send_message(chat_id, reply)

    return {"ok": True}

async def send_message(chat_id: int, text: str):
    async with httpx.AsyncClient() as client:
        await client.post(
            f"{TELEGRAM_API_URL}/sendMessage",
            json={"chat_id": chat_id, "text": text}
        )

@app.get("/")
def root():
    return {"message": "LEDYBOT Webhook is alive!"}

async def set_webhook():
    url = f"{BASE_URL}/telegram/{SECRET_TOKEN}"
    async with httpx.AsyncClient() as client:
        r = await client.post(
            f"{TELEGRAM_API_URL}/setWebhook",
            json={"url": url}
        )
        print("Webhook set status:", r.json())

if __name__ == "__main__":
    asyncio.run(set_webhook())
