# LEDYBOT Webhook Deployment

Этот проект содержит Telegram-бота LEDYBOT, развёрнутого с помощью FastAPI и Render.com. Работает в режиме webhook.

## Стартовая команда на Render:
```
uvicorn ledybot_webhook:app --host=0.0.0.0 --port=10000.
```

## Установка webhook:
Подставьте свой токен в ссылку:
```
https://api.telegram.org/bot<ВАШ_ТОКЕН>/setWebhook?url=https://ledybot-webhook.onrender.com/webhook/ledysecret12
```
