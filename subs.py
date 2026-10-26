import requests

urls = [
    "https://www.fotmob.com/api/matches",
    "https://www.fotmob.com/api/leagues",
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

        print("=" * 50, flush=True)
        print(url, flush=True)
        print("STATUS:", r.status_code, flush=True)
        print(r.text[:500], flush=True)

    except Exception as e:
        print(e, flush=True)