from models.db import db
from sqlalchemy_serializer import SerializerMixin

class ProfitShare(db.Model, SerializerMixin):
    __tablename__ = 'profit_shares'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    agreement_terms = db.Column(db.Text)

    project = db.relationship('Project', back_populates='profit_shares')
    user = db.relationship('User', back_populates='profit_shares')

    serialize_rules = ('-project.profit_shares', '-user.profit_shares')

    def __repr__(self):
        return f"<ProfitShare User: {self.user_id}, Amount: {self.amount}>"
