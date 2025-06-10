from models.db import db
from datetime import datetime
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

class Transaction(db.Model, SerializerMixin):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    description = db.Column(db.String(255), nullable=True)

    user = db.relationship('User', back_populates='transactions')

    serialize_rules = ('-user.transactions',)

    @validates('transaction_type')
    def validate_transaction_type(self, key, value):
        """Ensure the transaction type is valid."""
        valid_types = ['deposit', 'withdrawal', 'transfer', 'fee']
        if value not in valid_types:
            raise ValueError(f"Invalid transaction type. Must be one of {valid_types}.")
        return value

    @validates('amount')
    def validate_amount(self, key, value):
        """Ensure the transaction amount is positive."""
        if value <= 0:
            raise ValueError("Amount must be greater than zero.")
        return value

    def __repr__(self):
        return f"<Transaction {self.id}, {self.transaction_type}, Amount: {self.amount}, User ID: {self.user_id}, Created At: {self.created_at}>"
