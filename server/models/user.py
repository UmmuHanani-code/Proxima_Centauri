from sqlalchemy_serializer import SerializerMixin
from models.db import db
from datetime import datetime



class User(db.Model, SerializerMixin):
    __tablename__ = 'users'


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


    group_memberships = db.relationship('GroupMember', back_populates='user', cascade='all, delete-orphan')
    qards = db.relationship('Qard', back_populates='borrower', cascade='all, delete-orphan')
    profit_shares = db.relationship('ProfitShare', back_populates='user')

    serialize_rules = ('-group_memberships.user', '-qards.borrower',)


    def __repr__(self):
        return f"<User {self.id}, {self.username}, {self.email}, {self.created_at},{self.is_active}>"