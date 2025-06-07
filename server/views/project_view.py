from flask_restful import Resource, reqparse
from controllers.project_controller import ProjectController

class ProjectResourceView(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('group_id', type=int, required=True, help='Group ID is required')
    parser.add_argument('name', type=str, required=True, help='Project name is required')
    parser.add_argument('description', type=str)
    parser.add_argument('start_date', type=str)
    parser.add_argument('end_date', type=str)
    parser.add_argument('total_income', type=float)
    parser.add_argument('total_expenses', type=float)

    def get(self, project_id):
        return ProjectController.get_project(project_id), 200

    def put(self, project_id):
        data = ProjectResourceView.parser.parse_args()
        return ProjectController.update_project(project_id, data), 200

    def delete(self, project_id):
        return ProjectController.delete_project(project_id), 200

    def get(self):
        return ProjectController.get_all_projects(), 200

    def post(self):
        data = ProjectResourceView.parser.parse_args()
        return ProjectController.create_project(data), 201
