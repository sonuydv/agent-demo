from datetime import datetime

from pymongo import MongoClient


client = MongoClient("mongodb://root:passwd@127.0.0.1:27017/chatbot?directConnection=true&replicaSet=rs0&authSource=admin")
db = client["chatbot"]
collection = db["chat_history"]

# {chat_history:{user_id,messages:[]}}

def save_message(user_id:str,role:str,content:str):
    message = {
        "role":role,
        "content":content,
        "timestamp":datetime.now()
    }
    response = collection.update_one(
        {"user_id":user_id},
        {"$push":{"messages":message}},
        upsert=True
    )
    return response



def get_chat_history(user_id,limit=30):
    doc = collection.find_one({"user_id":user_id})
    if not doc:
        return []
    return doc["messages"][-limit:]