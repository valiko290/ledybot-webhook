# LEDYBOT Webhook Version

### 📌 Описание:
Это Telegram-бот LEDYBOT, подключённый через Webhook на FastAPI. Запускается на Render.

---

### ⚙️ Запуск на Render:

1. Создай новый Web Service на https://render.com
2. Подключи этот репозиторий
3. Укажи переменные окружения:
- BOT_TOKEN = <твой токен Telegram>
- BASE_URL = https://ledybot.onrender.com
- SECRET_TOKEN = supersecret

4. Укажи Start Command:
```
python ledybot_webhook.py
```

---

💡 После запуска Webhook установится автоматически и бот будет отвечать на /start и любые текстовые сообщения.
