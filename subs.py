import requests

r = requests.get(
    "https://www.fotmob.com/api/data/matches?date=20261026&timezone=Europe%2FBratislava&ccode3=SVK&includeNextDayLateNight=true",
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=15
)

print("STATUS:", r.status_code, flush=True)

data = r.json()

print(type(data), flush=True)
print(str(data)[:3000], flush=True)