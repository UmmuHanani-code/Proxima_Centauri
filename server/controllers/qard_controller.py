from flask import abort
from models import db, Qard

class QardController:
    @staticmethod
    def get_all_qards():
        qards = Qard.query.all()
        return [qard.to_dict() for qard in qards]

    @staticmethod
    def get_qard(qard_id):
        qard = Qard.query.get(qard_id)
        if not qard:
            abort(404, description="Qard not found")
        return qard.to_dict()

    @staticmethod
    def create_qard(data):
        qard = Qard(
            group_id=data['group_id'],
            borrower_id=data['borrower_id'],
            amount=data['amount'],
            reason=data.get('reason'),
            status=data.get('status', 'pending'),
            due_date=data.get('due_date')
        )
        db.session.add(qard)
        db.session.commit()
        return qard.to_dict()

    @staticmethod
    def update_qard(qard_id, data):
        qard = Qard.query.get(qard_id)
        if not qard:
            abort(404, description="Qard not found")

        qard.amount = data.get('amount', qard.amount)
        qard.reason = data.get('reason', qard.reason)
        qard.status = data.get('status', qard.status)
        qard.due_date = data.get('due_date', qard.due_date)
        db.session.commit()
        return qard.to_dict()

    @staticmethod
    def delete_qard(qard_id):
        qard = Qard.query.get(qard_id)
        if not qard:
            abort(404, description="Qard not found")
        db.session.delete(qard)
        db.session.commit()
        return {"message": "Qard deleted successfully"}
