import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Connect to MongoDB Atlas
client = MongoClient(os.getenv("MONGO_URI"))

# Select your database and collection
db = client["scraperDB"]
collection = db["books"]

# Retrieve and print documents
documents = collection.find()

print("📘 Stored Documents:")
for doc in documents:
    print(doc)
