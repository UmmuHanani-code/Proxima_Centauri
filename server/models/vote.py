from models.db import db
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime
from sqlalchemy.orm import validates


class Vote(db.Model, SerializerMixin):
    __tablename__ = 'votes'

    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    topic = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(50), default='open')  # open / closed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    group = db.relationship('Group', backref='votes')
    creator = db.relationship('User', backref='created_votes')

    serialize_rules = ('-group.votes', '-creator.created_votes', '-responses.vote',)

    @validates('status')
    def validate_status(self, key, value):
        if value not in ['open', 'closed']:
            raise ValueError("Status must be either 'open' or 'closed'")
        return value

    def __repr__(self):
        return f"<Vote {self.topic} by User {self.created_by}>"
