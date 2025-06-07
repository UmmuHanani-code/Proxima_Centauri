from flask_restful import Resource, reqparse
from controllers.vote_controller import VoteController

class VoteResourceView(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('group_id', type=int, required=True, help='Group ID is required')
    parser.add_argument('created_by', type=int, required=True, help='Created by is required')
    parser.add_argument('topic', type=str, required=True, help='Topic is required')
    parser.add_argument('description', type=str)
    parser.add_argument('status', type=str, choices=('open', 'closed'), default='open')

    def get(self, vote_id):
        return VoteController.get_vote(vote_id), 200

    def put(self, vote_id):
        data = VoteResourceView.parser.parse_args()
        return VoteController.update_vote(vote_id, data), 200

    def delete(self, vote_id):
        return VoteController.delete_vote(vote_id), 200

    def get(self):
        return VoteController.get_all_votes(), 200

    def post(self):
        data = VoteResourceView.parser.parse_args()
        return VoteController.create_vote(data), 201
