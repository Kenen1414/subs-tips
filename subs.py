import requests

url = "https://www.fotmob.com/api/data?date=20261026"

r = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=15
)

print("STATUS:", r.status_code, flush=True)
print(r.text[:1000], flush=True)