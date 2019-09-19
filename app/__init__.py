from flask import Flask
from flask_restplus import Api
from flask_pymongo import PyMongo
import config

app = Flask(__name__)
app.config['MONGO_URI'] = config.MONGO_URI

mongo = PyMongo(app)

api = Api(app, version='1.0', title='User API',
    description='API de usuario'    
)


from app.controllers.api_user import api_user
api.add_namespace(api_user)
