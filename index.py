from pymongo import MongoClient
from fastapi import FastAPI
from pydantic import BaseModel
import json


app = FastAPI()

client = MongoClient("mongodb+srv://Shreshika:Bunny234@cluster0.lzku1n5.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database("student")   # student is the database name
collection = db.studentdata  


class User(BaseModel):
    name : str
    age : int
    videos : int


@app.get('/')
async def find_all_users():
    data = []
    for i in collection.find():
        i['_id'] = str(i['_id'])
        data.append(i)
    return data

@app.post('/')
async def create_user(user : User):
    data = collection.insert_one(user.dict())
    inserted_user = collection.find_one({"_id": data.inserted_id})  # Retrieve the inserted user document
    inserted_user['_id'] = str(inserted_user['_id'])
    return inserted_user