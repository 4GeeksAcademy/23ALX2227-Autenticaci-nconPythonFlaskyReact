from flask import Flask, request, jsonify, Blueprint
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from api.models import db, User

api = Blueprint('api', __name__)
jwt = JWTManager()
bcrypt = Bcrypt()

# Configuración del JWT
def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'jwt_password'
    jwt.init_app(app)
    return app

CORS(api)

@api.route('/signup', methods=['POST'])
def create_user():
    body = request.get_json()
    raw_password = body.get('password')
    password_hash = bcrypt.generate_password_hash(raw_password).decode('utf-8')
    new_user = User(
        user_id=body['user_id'],
        name=body["name"],
        user_name=body["user_name"],
        email=body["email"],
        address=body["address"],
        phone=body["phone"],
        password=password_hash,  
        is_admin=body["is_admin"]
    )    
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "User created successfully", "user_added": new_user }), 200

@api.route('/login', methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    if not email or not password:
        return jsonify({"msg": "Bad email or password"}), 401
    
    existing_user = User.query.filter_by(email=email).first()  
    if not existing_user:
        return jsonify({"msg": "Email not found"}), 404
    
    password_hash = existing_user.password
    check_password = bcrypt.check_password_hash(password_hash, password)
    if not check_password:
        return jsonify({"msg": "Wrong password"}), 400
    
    user_id = existing_user.user_id  # Corregido aquí
    access_token = create_access_token(identity=user_id)
    return jsonify({"access_token": access_token, "msg": "Access Success"}), 200
    

@api.route('/private', methods=['GET'])
@jwt_required()
def get_user():
    current_user_id = get_jwt_identity()  
    if current_user_id:
        users = User.query.all()
        users_list = [{"id": user.user_id, "email": user.email} for user in users]  # Corregido aquí
        return jsonify(users_list), 200
    else:
        return jsonify({"Error": "Invalid or missing token"}), 401

@api.route('/user', methods=['GET'])
def get_all_users():
    users = User.query.all()
    if not users:
        return jsonify({"msg": "Not found"}), 404
    serialized_users = [user.serialize() for user in users] 
    return jsonify(serialized_users), 200

@api.route('/user/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"msg": f"User with id {user_id} not found"}), 404
    serialized_user = user.serialize()  
    return jsonify(serialized_user), 200