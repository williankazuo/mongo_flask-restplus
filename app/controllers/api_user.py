from flask import request
from flask_restplus import Namespace, Resource, fields
from app.handlers.user_handler import get_all_users, insert_user, delete_user, update_user, get_user_by_id
import json
from bson import json_util


api_user = Namespace("Usuario", path="/user")

user_post_model = api_user.model(
    "user_post", {
        "usuario": fields.String(description="Usuário do sistema", required=True),
        "nome": fields.String(description="Nome do usuário do sistema", required=True),
        "cpf": fields.String(description="Nome do usuário do sistema", required=True)
    }
)

user_put_model = api_user.model(
    "user_put", {
        "usuario": fields.String(description="Usuário do sistema", required=False),
        "nome": fields.String(description="Nome do usuário do sistema", required=False),
        "cpf": fields.String(description="Nome do usuário do sistema", required=False)
    }
)

@api_user.route('/')
class User(Resource):
    def get(self):
        response, code = get_all_users()
        return response, code

    @api_user.expect(user_post_model)
    def post(self):
        response, code = insert_user(request.json)
        return response, code


@api_user.route('/<string:id>')
class UserId(Resource):
    def get(self, id):
        response, code = get_user_by_id(id)
        return response, code

    def delete(self, id):
        response, code = delete_user(id)
        return response, code

    @api_user.expect(user_put_model)
    def put(self, id):
        response, code = update_user(id, request.json)
        return response, code