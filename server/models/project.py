from models.db import db
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

class Project(db.Model, SerializerMixin):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    total_income = db.Column(db.Float, default=0.0)
    total_expenses = db.Column(db.Float, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    group = db.relationship('Group', back_populates='projects')
    profit_shares = db.relationship('ProfitShare', back_populates='project', cascade='all, delete-orphan')

    serialize_rules = ('-group.projects', '-profit_shares.project')

    def __repr__(self):
        return f"<Project {self.name}, Group: {self.group_id}, Income: {self.total_income}>"
