import requests
from flask import Flask
from pymongo import MongoClient
import requests
import threading
import json

url = 'http://localhost:5000'

app = Flask(__name__)

client = MongoClient('mongodb+srv://nhan0812:nhan0812@cluster0.2zdl7ac.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

def monitor_changes():
    with client.watch() as stream:
        for change in stream:
            print(f"Change detected: {change}")
            if change['operationType'] == 'insert':
                requests.post(url, data = json.dumps({"operationType": change['operationType'], "name": change['fullDocument']['name'], "link": change['fullDocument']['link'], "time": change['wallTime'].isoformat()}), headers= {"Content-Type": "application/json"})
            elif change['operationType'] == 'delete':
                requests.post(url, data = json.dumps({"operationType": change['operationType'], "time": change['wallTime'].isoformat()}), headers= {"Content-Type": "application/json"})
            elif change['operationType'] == 'update':
                requests.post(url, data = json.dumps({"operationType": change['operationType'], "time": change['wallTime'].isoformat()}), headers= {"Content-Type": "application/json"})

thread = threading.Thread(target=monitor_changes)
thread.start()

@app.route('/')
def index():
    return "Monitoring MongoDB for changes..."

if __name__ == '__main__':
    app.run(port=5001)
