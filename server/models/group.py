from models.db import db
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

class Group(db.Model, SerializerMixin):
    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    members = db.relationship('GroupMember', back_populates='group', cascade='all, delete-orphan')
    qards = db.relationship('Qard', back_populates='group', cascade='all, delete-orphan')
    projects = db.relationship('Project', back_populates='group', cascade='all, delete-orphan')

    serialize_rules = ('-members', '-qards', '-projects')


    def __repr__(self):
        return f"<Group {self.id}, {self.name}, {self.description}, {self.created_at}>"