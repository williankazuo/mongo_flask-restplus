import os

HOST = '0.0.0.0'
PORT = '5000'
DEBUG = True
MONGO_URI = f'mongodb://{os.environ.get("MONGO_URL", "localhost")}/db_user'