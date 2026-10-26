import requests

match_id = 5802972

r = requests.get(
    f"https://www.fotmob.com/api/data/matchDetails?matchId={match_id}",
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=15
)

data = r.json()

events = (
    data.get("content", {})
    .get("matchFacts", {})
    .get("events", {})
    .get("events", [])
)

print("EVENT COUNT:", len(events), flush=True)

for event in events:
    print(event, flush=True)