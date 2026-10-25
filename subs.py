import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

print("BOT STARTED")

r = requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    json={
        "chat_id": CHANNEL_ID,
        "text": "🚀 TEST START"
    }
)

print(r.status_code)
print(r.text)

input("STOP")