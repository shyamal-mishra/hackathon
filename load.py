import json
from pymongo import MongoClient

# Define MongoDB connection URI
mongo_uri = 'mongodb+srv://sm4825:VDSIdNRsYU9v9EVr@cluster0.gvo92qb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

# Define the name of your MongoDB database and collection
db_name = 'test-db'
collection_name = 'test-connection'

# Read the JSON file
with open('data.json') as f:
    data = json.load(f)

# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client[db_name]
collection = db[collection_name]

# Insert data into MongoDB
collection.insert_many(data)

print("Data inserted successfully!")
