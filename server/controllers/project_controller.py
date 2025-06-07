from flask import abort
from models import db, Project

class ProjectController:
    @staticmethod
    def get_all_projects():
        projects = Project.query.all()
        return [project.to_dict() for project in projects]

    @staticmethod
    def get_project(project_id):
        project = Project.query.get(project_id)
        if not project:
            abort(404, description="Project not found")
        return project.to_dict()

    @staticmethod
    def create_project(data):
        project = Project(
            group_id=data['group_id'],
            name=data['name'],
            description=data.get('description'),
            start_date=data.get('start_date'),
            end_date=data.get('end_date'),
            total_income=data.get('total_income', 0.0),
            total_expenses=data.get('total_expenses', 0.0)
        )
        db.session.add(project)
        db.session.commit()
        return project.to_dict()

    @staticmethod
    def update_project(project_id, data):
        project = Project.query.get(project_id)
        if not project:
            abort(404, description="Project not found")

        project.name = data.get('name', project.name)
        project.description = data.get('description', project.description)
        project.start_date = data.get('start_date', project.start_date)
        project.end_date = data.get('end_date', project.end_date)
        project.total_income = data.get('total_income', project.total_income)
        project.total_expenses = data.get('total_expenses', project.total_expenses)
        db.session.commit()
        return project.to_dict()

    @staticmethod
    def delete_project(project_id):
        project = Project.query.get(project_id)
        if not project:
            abort(404, description="Project not found")
        db.session.delete(project)
        db.session.commit()
        return {"message": "Project deleted successfully"}
