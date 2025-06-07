from flask_restful import Resource, reqparse
from controllers.user_controller import UserController

class UserResourceView(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='Username is required')
    parser.add_argument('email', type=str, required=True, help='Email is required')
    parser.add_argument('password', type=str, required=True, help='Password is required')
    parser.add_argument('is_active', type=bool, required=False)

    def get(self, user_id):
        return UserController.get_user(user_id), 200

    def put(self, user_id):
        data = UserResourceView.parser.parse_args()
        return UserController.update_user(user_id, data), 200

    def delete(self, user_id):
        return UserController.delete_user(user_id), 200

    def get(self):
        return UserController.get_all_users(), 200

    def post(self):
        data = UserResourceView.parser.parse_args()
        return UserController.create_user(data), 201
