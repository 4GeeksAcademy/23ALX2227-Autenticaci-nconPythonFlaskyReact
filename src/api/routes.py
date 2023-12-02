"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extend import JWTManager, create_access_token, jwt_required, get_jwt_identy
import json
import bcrypt



api = Blueprint('api', __name__)

api.config["JWT_SECRET_KEY"] = "jwt_password" 
jwt = JWTManager(api)

# Allow CORS requests to this API
CORS(api)

@api.route('/singup', methods=['POST'])
def create_user():
    body = json.loads(request.data)
    # body = request.json()
    raw_password = request.json.get('password')
    password_hash = bcrypt.generate_password_hash(raw_password).decode('utf-8')
    new_user = User(
        user_id = body['user_id'],
        name = body["name"],
        user_name = body["user_name"],
        email = body["email"],
        address = body["address"],
        phone = body["phone"],
        password = body[{password_hash}],        
        is_admin = body["is_admin"]
    )    
    
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "user created succesfull", "user_added": new_user }), 200

@api.route('/login', methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    if not email or not password:
        return jsonify({"msg": "Bad email or password"}), 401
    existing_user = User.query.filter_by(email = email).firt()
    if not existing_user:
        return jsonify({"msg": "Email not found"})
    password_hash = existing_user.password
    true_or_fale = bcrypt.check_password_hash(password_hash, password)
    if not true_or_fale:
        return jsonify({"msg": "Wrong password "}), 400
    
    user_id = existing_user.id
    access_token = create_access_token(identity = user_id)
    return jsonify({"access_token": access_token, "msg": "Access Success"}), 200
    

@api.route('/private', methods=['GET'])
@jwt_required()
def get_user():
    currents_user_id = get_jwt_identy()
    if currents_user_id:
        users = User.query.all()
        users_list = []
        for user in users:
            users_dict = {
                'id': 'user_id',
                'email': 'user.email'
            }
            users_list.append(users_dict)
        return jsonify(users_list), 200
    else:
        return {"Error": "Token inválido o no proporcionado"}, 401
    return jsonify({"msg": "It works"})


@api.route('/user', methods=['GET'])
def get_all_users():
    users = User.query.all()
    if len(users) < 1:
        return jsonify({"msg": "not found"}), 404
    serialized_users = [x.serialize() for x in users]
    return serialized_users, 200

@api.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"msg": f"User with id {user_id} not found"}), 404
    serialized_user = user.serielized()
    return serialized_user , 200