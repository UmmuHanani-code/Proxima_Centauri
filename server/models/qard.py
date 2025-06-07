from models.db import db
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

class Qard(db.Model, SerializerMixin):
    __tablename__ = 'qards'

    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    borrower_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    reason = db.Column(db.Text)
    status = db.Column(db.String(50), default='pending')
    due_date = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    group = db.relationship('Group', back_populates='qards')
    borrower = db.relationship('User', back_populates='qards')

    serialize_rules = ('-group.qards', '-borrower.qards')

    def __repr__(self):
        return f"<Qard {self.id}, Amount: {self.amount}, Reason: {self.reason}, Status: {self.status}, Due Date: {self.due_date}, Created At: {self.created_at}>"
