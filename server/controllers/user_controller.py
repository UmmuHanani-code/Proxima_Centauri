from models import db, User
from werkzeug.security import generate_password_hash
from flask import abort

class UserController:

    @staticmethod
    def get_all_users():
        users = User.query.all()
        return [user.to_dict() for user in users]

    @staticmethod
    def get_user(user_id):
        user = User.query.get(user_id)
        if not user:
            abort(404, description="User not found")
        return user.to_dict()

    @staticmethod
    def create_user(data):
        if User.query.filter_by(email=data['email']).first():
            abort(400, description="Email already exists")

        hashed_password = generate_password_hash(data['password'])

        new_user = User(
            username=data['username'],
            email=data['email'],
            password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()

        return new_user.to_dict()

    @staticmethod
    def update_user(user_id, data):
        user = User.query.get(user_id)
        if not user:
            abort(404, description="User not found")

        if 'email' in data and data['email'] != user.email and User.query.filter_by(email=data['email']).first():
            abort(400, description="Email already exists")

        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        user.password = generate_password_hash(data['password']) if 'password' in data else user.password
        db.session.commit()

        return user.to_dict()

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if not user:
            abort(404, description="User not found")

        db.session.delete(user)
        db.session.commit()

        return {"message": "User deleted successfully"}
