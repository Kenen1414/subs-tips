import requests
import os
import time

BOT_TOKEN = os.getenv("8553880830:AAHsv3uIYFrI_LcvMJ27ZCDwM5A9719NPMA")
CHANNEL_ID = os.getenv("-1003500029930")

requests.post(
    f"https://api.telegram.org/bot{8553880830:AAHsv3uIYFrI_LcvMJ27ZCDwM5A9719NPMA}/sendMessage",
    json={
        "chat_id": -1003500029930,
        "text": "✅ Railway bot je online"
    }
)

while True:
    time.sleep(60)