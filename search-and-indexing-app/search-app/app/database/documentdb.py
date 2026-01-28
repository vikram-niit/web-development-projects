from pymongo import MongoClient
import os

client = MongoClient(os.getenv("DOCUMENTDB_URI"))
db = client["searchdb"]
products_collection = db["products"]
