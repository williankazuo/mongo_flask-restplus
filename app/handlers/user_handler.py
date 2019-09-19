from app import mongo
from bson.json_util import dumps

def insert_user(data):
    response = mongo.db.users.insert(data)
    return response


def get_all_users():
    data_users = mongo.db.users.find({})
    return data_users
        