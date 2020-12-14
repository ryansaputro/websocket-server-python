import requests

url = "http://127.0.0.1:8000/api/v1/sync"
res = requests.get(url)

print(res.status_code)