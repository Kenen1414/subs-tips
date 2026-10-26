import requests

urls = [
    "https://www.fotmob.com/api/leagues?id=47",
    "https://www.fotmob.com/api/matchDetails?matchId=1",
    "https://www.fotmob.com/api/teams?id=8456",
]

for url in urls:

    try:

        r = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=15
        )

        print("=" * 50)
        print(url)
        print("STATUS:", r.status_code)
        print(r.text[:1000])

    except Exception as e:
        print(e)