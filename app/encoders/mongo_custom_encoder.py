from datetime import datetime
from bson import ObjectId

def encodeMongo(obj):
    for prop in obj:
        if isinstance(obj[prop], ObjectId):
            obj[prop] = str(obj[prop])
        elif isinstance(obj[prop], datetime):
            obj[prop] = str(obj[prop])
    return obj
