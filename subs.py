import requests

urls = [
    "https://www.fotmob.com/api",
    "https://www.fotmob.com/api/data",
    "https://www.fotmob.com/api/matches",
    "https://www.fotmob.com/api/leagues"
]

for url in urls:
    try:
        r = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=15
        )

        print("=" * 50)
        print(url)
        print("STATUS:", r.status_code)

    except Exception as e:
        print(url, e)