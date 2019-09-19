from flask import request
from flask_restplus import Namespace, Resource, fields
from app.handlers.user_handler import get_all_users, insert_user
import json
from bson import json_util
from app.encoders.mongo_custom_encoder import encodeMongo

api_user = Namespace("user", path="/user")

user_post_model = api_user.model(
    "User",
    {
        "username": fields.String(description="Usuário do sistema", required=True),
        "fullname": fields.String(description="Nome do usuário do sistema", required=True),
    },
)


@api_user.route("/")
class User(Resource):
    def get(self):
        users = get_all_users()
        response = [encodeMongo(user) for user in users]
        return response, 200

    @api_user.expect(user_post_model)
    def post(self):
        user_id = insert_user(request.json)
        return user_id, 200

    def put(self, id):
        return request.json
