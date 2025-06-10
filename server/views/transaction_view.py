from flask_restful import Resource, reqparse
from controllers.transaction_controller import TransactionController

class TransactionResourceView(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('amount', type=float, required=True, help='Amount is required')
    parser.add_argument('transaction_type', type=str, required=True, help='Transaction type is required')  # Deposit, Withdrawal, etc.
    parser.add_argument('user_id', type=int, required=True, help='User ID is required')

    def get(self, transaction_id):
        return TransactionController.get_transaction(transaction_id), 200

    def put(self, transaction_id):
        data = TransactionResourceView.parser.parse_args()
        return TransactionController.update_transaction(transaction_id, data), 200

    def delete(self, transaction_id):
        return TransactionController.delete_transaction(transaction_id), 200

    def get(self):
        return TransactionController.get_all_transactions(), 200

    def post(self):
        data = TransactionResourceView.parser.parse_args()
        return TransactionController.create_transaction(data), 201