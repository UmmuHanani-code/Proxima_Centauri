from flask_restful import Resource, reqparse
from controllers.group_controller import GroupController

class GroupResourceView(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Group name is required')
    parser.add_argument('description', type=str, required=False)

    def get(self, group_id):
        return GroupController.get_group(group_id), 200

    def put(self, group_id):
        data = GroupResourceView.parser.parse_args()
        return GroupController.update_group(group_id, data), 200

    def delete(self, group_id):
        return GroupController.delete_group(group_id), 200

    def get(self):
        return GroupController.get_all_groups(), 200

    def post(self):
        data = GroupResourceView.parser.parse_args()
        return GroupController.create_group(data), 201
