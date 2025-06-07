from flask_restful import Resource, reqparse
from controllers.qard_controller import QardController

class QardResourceView(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('group_id', type=int, required=True, help='Group ID is required')
    parser.add_argument('borrower_id', type=int, required=True, help='Borrower ID is required')
    parser.add_argument('amount', type=float, required=True, help='Amount is required')
    parser.add_argument('reason', type=str)
    parser.add_argument('status', type=str, choices=('pending', 'approved', 'repaid'), default='pending')
    parser.add_argument('due_date', type=str)

    def get(self, qard_id):
        return QardController.get_qard(qard_id), 200

    def put(self, qard_id):
        data = QardResourceView.parser.parse_args()
        return QardController.update_qard(qard_id, data), 200

    def delete(self, qard_id):
        return QardController.delete_qard(qard_id), 200

    def get(self):
        return QardController.get_all_qards(), 200

    def post(self):
        data = QardResourceView.parser.parse_args()
        return QardController.create_qard(data), 201
