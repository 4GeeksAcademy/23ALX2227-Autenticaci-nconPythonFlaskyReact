from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique= True)
    user_name = db.Column(db.String(50), unique= True)
    email = db.Column(db.String(120), unique=True, nullable=False)    
    address = db.Column(db.String(80), unique=False, nullable=False)
    phone = db.Column(db.String(80), unique=False, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_admin = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "user_name": self.user_name,
            "email": self.email,
            "address": self.address,
            "phone": self.phone,
            "is_admin": self.is_admin
            # do not serialize the password, its a security breach
        }