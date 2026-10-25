import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

print("BOT STARTED", flush=True)

r = requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    json={
        "chat_id": CHANNEL_ID,
        "text": "🚀 TEST BOT STARTED"
    }
)

print(r.status_code, flush=True)
print(r.text, flush=True)

while True:
    pass