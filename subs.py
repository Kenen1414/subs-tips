from playwright.sync_api import sync_playwright
import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

def send_message(text):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={
            "chat_id": CHANNEL_ID,
            "text": text
        }
    )

try:
    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True,
            args=["--no-sandbox"]
        )

        page = browser.new_page()

        page.goto(
            "https://www.google.com",
            wait_until="domcontentloaded"
        )

        title = page.title()

        send_message(
            f"✅ PLAYWRIGHT OK\n\n{title}"
        )

        print(title, flush=True)

        browser.close()

except Exception as e:

    print(e, flush=True)

    send_message(
        f"❌ PLAYWRIGHT ERROR\n\n{e}"
    )
