from flask import Flask
from pymongo import MongoClient


client = MongoClient('mongodb+srv://nhan0812:nhan0812@cluster0.2zdl7ac.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
dtb = client['Rickroll']
collection = dtb['Rickroll']

data = {
    "name": "Random Video",
    "link": "https://www.youtube.com/watch?v=PfIbXTsNGac"
}

def add_item():
    collection.insert_one(data)
    print("Item added successfully!")

add_item()