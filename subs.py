import requests

r = requests.get(
    "https://www.fotmob.com/api/data/matches?date=20261026&timezone=Europe%2FBratislava&ccode3=SVK&includeNextDayLateNight=true",
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=15
)

data = r.json()

for league in data.get("leagues", []):
    for match in league.get("matches", []):

        if not match["status"].get("ongoing", False):
            continue

        match_id = match["id"]

        details = requests.get(
            f"https://www.fotmob.com/api/data/matchDetails?matchId={match_id}",
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=15
        ).json()

        events = (
            details.get("content", {})
            .get("matchFacts", {})
            .get("events", {})
            .get("events", [])
        )

        print("\n")
        print("=" * 50)
        print(match["home"]["name"], "vs", match["away"]["name"])
        print("MATCH:", match_id)

        for event in events:
            print(event.get("type"), event.get("time"))