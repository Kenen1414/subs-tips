from playwright.sync_api import sync_playwright
import os
import requests

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

print("PLAYWRIGHT START", flush=True)

try:
    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page()

        page.goto(
            "https://www.sofascore.com/football",
            wait_until="domcontentloaded",
            timeout=60000
        )

        title = page.title()

        print(title, flush=True)

        send_message(
            f"✅ Playwright funguje\n\nTitle: {title}"
        )

        browser.close()

except Exception as e:
    print(e, flush=True)

    send_message(
        f"❌ Playwright chyba\n\n{e}"
    )