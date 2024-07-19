import requests
import json

url = 'https://e8cd-115-73-184-90.ngrok-free.app'

data = {
    'name': 'Rick Astley - Never Gonna Give You Up (Official Music Video)',
    'link': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
}

r = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

print(f"Response: {r.status_code}")
