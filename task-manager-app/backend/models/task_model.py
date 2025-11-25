from pymongo import MongoClient
import config
from bson.objectid import ObjectId

client = MongoClient(config.MONGO_URI)
db = client.task_manager
tasks_collection = db.tasks

class Task:
    @staticmethod
    def get_all():
        return list(tasks_collection.find())

    @staticmethod
    def create(data):
        return tasks_collection.insert_one(data).inserted_id

    @staticmethod
    def delete(task_id):
        return tasks_collection.delete_one({"_id": ObjectId(task_id)})
