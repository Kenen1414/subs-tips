import requests

r = requests.get(
    "https://www.fotmob.com/api",
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=15
)

print("STATUS:", r.status_code, flush=True)
print(r.text[:5000], flush=True)