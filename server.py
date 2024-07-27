import requests
from flask import Flask
from pymongo import MongoClient
import requests
import threading
import json

url = ' https://90c6-115-77-190-72.ngrok-free.app'

app = Flask(__name__)

client = MongoClient('mongodb+srv://nhan0812:nhan0812@cluster0.2zdl7ac.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

def monitor_changes():
    with client.watch() as stream:
        for change in stream:
            print(f"Change detected: {change}")
            requests.post(url, data = json.dumps({"operationType": change['operationType']}), headers= {"Content-Type": "application/json"})

# Run the monitor_changes function in a separate thread
thread = threading.Thread(target=monitor_changes)
thread.start()

@app.route('/')
def index():
    return "Monitoring MongoDB for changes..."

if __name__ == '__main__':
    app.run(port=5001)
