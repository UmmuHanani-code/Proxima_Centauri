from flask import abort
from models import db, Transaction

class TransactionController:
    @staticmethod
    def get_all_transactions():
        transactions = Transaction.query.all()
        return [transaction.to_dict() for transaction in transactions]

    @staticmethod
    def get_transaction(transaction_id):
        transaction = Transaction.query.get(transaction_id)
        if not transaction:
            abort(404, description="Transaction not found")
        return transaction.to_dict()

    @staticmethod
    def create_transaction(data):
        transaction = Transaction(
            amount=data['amount'],
            transaction_type=data['transaction_type'],
            user_id=data['user_id']
        )
        db.session.add(transaction)
        db.session.commit()
        return transaction.to_dict()

    @staticmethod
    def update_transaction(transaction_id, data):
        transaction = Transaction.query.get(transaction_id)
        if not transaction:
          abort(404, description="Transaction not found")


        transaction.amount = data.get('amount', transaction.amount)
        transaction.transaction_type = data.get('transaction_type', transaction.transaction_type)
        db.session.commit()
        return transaction.to_dict()

    @staticmethod
    def delete_transaction(transaction_id):
        transaction = Transaction.query.get(transaction_id)
        if not transaction:
            abort(404, description="Transaction not found")

        db.session.delete(transaction)
        db.session.commit()
        return {"message": "Transaction deleted successfully"}  
