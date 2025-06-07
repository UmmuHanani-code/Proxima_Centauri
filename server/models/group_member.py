from models.db import db
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

class GroupMember(db.Model, SerializerMixin):
    __tablename__ = 'group_members'

    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    role = db.Column(db.String(50), default='member')
    joined_at = db.Column(db.DateTime, server_default=db.func.now())


    user = db.relationship('User', back_populates='group_memberships')
    group = db.relationship('Group', back_populates='members')

    serialize_rules = ('-user.group_memberships', '-group.members',)


    def __repr__(self):
        return f"<GroupMember {self.id}, {self.role}, {self.joined_at}>"