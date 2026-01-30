from pymongo import MongoClient
import os

uri = os.getenv("DOCUMENTDB_URI")
print(f"uri = {uri}")

client = MongoClient(
    uri,
    tls=True,
    tlsAllowInvalidCertificates=True,
    retryWrites=False,
    serverSelectionTimeoutMS=5000,
    connectTimeoutMS=5000,
    socketTimeoutMS=5000
)

db = client["searchdb"]

print(db.command("ping"))
print(db.products.count_documents({}))
