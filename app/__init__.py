from flask import Flask, Blueprint
from flask_restplus import Api
from flask_pymongo import PyMongo
import config

app = Flask(__name__)
app.config['MONGO_URI'] = config.MONGO_URI

mongo = PyMongo(app)

blueprint = Blueprint('api', __name__, url_prefix='/api/v1') 

api = Api(blueprint, version='1.0', title='User API',
    description='API de usuario'    
)

app.register_blueprint(blueprint)

from app.controllers.api_user import api_user
api.add_namespace(api_user)
