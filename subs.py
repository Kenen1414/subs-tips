import requests
import os
import time
from datetime import datetime

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

sent_events = set()


def send_message(text):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={
            "chat_id": CHANNEL_ID,
            "text": text
        },
        timeout=10
    )


print("FOTMOB BOT STARTED", flush=True)
send_message("🚀 FOTMOB BOT STARTED")

while True:
    try:

        today = datetime.now().strftime("%Y%m%d")

        matches_data = requests.get(
            f"https://www.fotmob.com/api/data/matches?date={today}&timezone=Europe%2FBratislava&ccode3=SVK&includeNextDayLateNight=true",
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=15
        ).json()

        for league in matches_data.get("leagues", []):

            for match in league.get("matches", []):

                status = match.get("status", {})

                if not status.get("ongoing", False):
                    continue

                match_id = match["id"]

                home = match["home"]["name"]
                away = match["away"]["name"]

                details = requests.get(
                    f"https://www.fotmob.com/api/data/matchDetails?matchId={match_id}",
                    headers={
                        "User-Agent": "Mozilla/5.0"
                    },
                    timeout=15
                ).json()

                events = (
                    details.get("content", {})
                    .get("matchFacts", {})
                    .get("events", {})
                    .get("events", [])
                )

                for event in events:

                    event_type = str(event.get("type", "")).lower()

                    # Tu uvidíme ako FotMob označuje striedanie
                    print(event_type, flush=True)

                    if "sub" not in event_type:
                        continue

                    minute = event.get("time", 0)

                    if minute > 45:
                        continue

                    event_id = event.get("eventId")

                    key = f"{match_id}_{event_id}"

                    if key in sent_events:
                        continue

                    player_name = event.get("nameStr", "")

                    text = (
                        f"🔄 STRIEDANIE V 1. POLČASE\n\n"
                        f"⚽ {home} vs {away}\n"
                        f"⏱️ {minute}'\n\n"
                        f"{player_name}"
                    )

                    send_message(text)

                    print(text, flush=True)

                    sent_events.add(key)

        time.sleep(30)

    except Exception as e:
        print("ERROR:", e, flush=True)
        time.sleep(60)