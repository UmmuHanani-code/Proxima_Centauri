from flask import abort
from models import db, ProfitShare

class ProfitShareController:
    @staticmethod
    def get_all_profit_shares():
        profit_shares = ProfitShare.query.all()
        return [profit_share.to_dict() for profit_share in profit_shares]

    @staticmethod
    def get_profit_share(profit_share_id):
        profit_share = ProfitShare.query.get(profit_share_id)
        if not profit_share:
            abort(404, description="ProfitShare not found")
        return profit_share.to_dict()

    @staticmethod
    def create_profit_share(data):
        profit_share = ProfitShare(
            project_id=data['project_id'],
            user_id=data['user_id'],
            amount=data['amount'],
            agreement_terms=data.get('agreement_terms')
        )
        db.session.add(profit_share)
        db.session.commit()
        return profit_share.to_dict()

    @staticmethod
    def update_profit_share(profit_share_id, data):
        profit_share = ProfitShare.query.get(profit_share_id)
        if not profit_share:
            abort(404, description="ProfitShare not found")

        profit_share.amount = data.get('amount', profit_share.amount)
        profit_share.agreement_terms = data.get('agreement_terms', profit_share.agreement_terms)
        db.session.commit()
        return profit_share.to_dict()

    @staticmethod
    def delete_profit_share(profit_share_id):
        profit_share = ProfitShare.query.get(profit_share_id)
        if not profit_share:
            abort(404, description="ProfitShare not found")
        db.session.delete(profit_share)
        db.session.commit()
        return {"message": "ProfitShare deleted successfully"}
