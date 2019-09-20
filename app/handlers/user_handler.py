from app import mongo
from app.encoders.mongo_custom_encoder import encodeMongo
from bson import ObjectId
from datetime import datetime

def insert_user(data):
    cpf = str(data['cpf'])
    result = mongo.db.users.find_one({'cpf' : cpf})
    if result is None:
        data['created_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data['update_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = mongo.db.users.insert(data)

        data['_id'] = str(result)

        return data, 200
    
    return {'message': f'Usuário já cadastrado com esse cpf: {cpf}'}, 400
    

def get_all_users():
    result = mongo.db.users.find({})
    response = [encodeMongo(user) for user in result]

    return response, 200

def get_user_by_id(id):
    result = mongo.db.users.find_one({'_id' : ObjectId(id)})
    if result is None:
        return {'message': f'Usuário não encontrado'}, 404

    return encodeMongo(result), 200

def delete_user(id):
    try:
        result = mongo.db.users.delete_one({'_id': ObjectId(id)})
        if result.deleted_count is not 1:
            return {'message': f'Id não encontrado'}, 404
        else:
            return {'_id' : f'{id}'}, 200
    except Exception as e:
        print(f'Error: {e}')

    return {'message': f'Erro ao deletar usuário'}, 400

def update_user(id, data):
    pass