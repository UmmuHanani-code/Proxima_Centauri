from flask import abort
from models import db, Vote

class VoteController:
    @staticmethod
    def get_all_votes():
        votes = Vote.query.all()
        return [vote.to_dict() for vote in votes]

    @staticmethod
    def get_vote(vote_id):
        vote = Vote.query.get(vote_id)
        if not vote:
            abort(404, description="Vote not found")
        return vote.to_dict()

    @staticmethod
    def create_vote(data):
        vote = Vote(
            group_id=data['group_id'],
            created_by=data['created_by'],
            topic=data['topic'],
            description=data.get('description'),
            status=data.get('status', 'open')
        )
        db.session.add(vote)
        db.session.commit()
        return vote.to_dict()

    @staticmethod
    def update_vote(vote_id, data):
        vote = Vote.query.get(vote_id)
        if not vote:
            abort(404, description="Vote not found")

        vote.topic = data.get('topic', vote.topic)
        vote.description = data.get('description', vote.description)
        vote.status = data.get('status', vote.status)
        db.session.commit()
        return vote.to_dict()

    @staticmethod
    def delete_vote(vote_id):
        vote = Vote.query.get(vote_id)
        if not vote:
            abort(404, description="Vote not found")
        db.session.delete(vote)
        db.session.commit()
        return {"message": "Vote deleted successfully"}
