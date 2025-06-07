from models import db, Group
from flask import abort

class GroupController:
    @staticmethod
    def get_all_groups():
        groups = Group.query.all()
        return [group.to_dict() for group in groups]

    @staticmethod
    def get_group(group_id):
        group = Group.query.get(group_id)
        if not group:
            abort(404, description="Group not found")
        return group.to_dict()

    @staticmethod
    def create_group(data):
        if Group.query.filter_by(name=data['name']).first():
            abort(400, description="Group name already exists")

        group = Group(
            name=data['name'],
            description=data.get('description', '')  
        )
        db.session.add(group)
        db.session.commit()
        return group.to_dict()

    @staticmethod
    def update_group(group_id, data):
        group = Group.query.get(group_id)
        if not group:
            abort(404, description="Group not found")

        group.name = data.get('name', group.name)
        group.description = data.get('description', group.description)
        db.session.commit()
        return group.to_dict()

    @staticmethod
    def delete_group(group_id):
        group = Group.query.get(group_id)
        if not group:
            abort(404, description="Group not found")

        db.session.delete(group)
        db.session.commit()
        return {"message": "Group deleted successfully"}
