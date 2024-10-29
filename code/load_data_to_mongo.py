from pymongo import MongoClient
import json

# Connect to MongoDB (adjust the URI if using a remote MongoDB server)
client = MongoClient('mongodb://localhost:27017/')
db = client['DisasterResponseDB']  # Database name
collection = db['EmergencyPosts']  # Collection name

# Load JSON data
with open('output_posts_data.json', 'r') as f:
    data = json.load(f)

# Insert data into MongoDB
collection.insert_many(data)
print("Data has been successfully inserted into MongoDB.")
