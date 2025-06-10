from flask_restful import Resource, reqparse
from controllers.profit_controller import ProfitShareController

class ProfitShareResourceView(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('project_id', type=int, required=True, help='Project ID is required')
    parser.add_argument('user_id', type=int, required=True, help='User ID is required')
    parser.add_argument('amount', type=float, required=True, help='Amount is required')
    parser.add_argument('agreement_terms', type=str)

    def get(self, profit_share_id):
        return ProfitShareController.get_profit_share(profit_share_id), 200

    def put(self, profit_share_id):
        data = ProfitShareResourceView.parser.parse_args()
        return ProfitShareController.update_profit_share(profit_share_id, data), 200

    def delete(self, profit_share_id):
        return ProfitShareController.delete_profit_share(profit_share_id), 200

    def get(self):
        return ProfitShareController.get_all_profit_shares(), 200

    def post(self):
        data = ProfitShareResourceView.parser.parse_args()
        return ProfitShareController.create_profit_share(data), 201
