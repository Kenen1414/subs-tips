import requests
import os
import time

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

sent_events = set()

def send_message(text):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={
            "chat_id": CHANNEL_ID,
            "text": text
        }
    )

print("SOFASCORE BOT STARTED", flush=True)

while True:
    try:
        live = requests.get(
            "https://api.sofascore.com/api/v1/sport/football/events/live",
            headers={"User-Agent": "Mozilla/5.0"}
        ).json()

        print(f"LIVE MATCHES: {len(live.get('events', []))}", flush=True)

        for match in live.get("events", []):

            event_id = match["id"]

            incidents = requests.get(
                f"https://api.sofascore.com/api/v1/event/{event_id}/incidents",
                headers={"User-Agent": "Mozilla/5.0"}
            ).json()

            for incident in incidents.get("incidents", []):

                if incident.get("incidentType") != "substitution":
                    continue

                minute = incident.get("time", 0)

                if minute > 45:
                    continue

                key = f"{event_id}_{minute}"

                if key in sent_events:
                    continue

                home = match["homeTeam"]["name"]
                away = match["awayTeam"]["name"]

                text = (
                    f"🔄 STRIEDANIE V 1. POLČASE\n\n"
                    f"⚽ {home} vs {away}\n"
                    f"⏱️ {minute}'"
                )

                send_message(text)

                print(text, flush=True)

                sent_events.add(key)

        time.sleep(15)

    except Exception as e:
        print("ERROR:", e, flush=True)
        time.sleep(30)