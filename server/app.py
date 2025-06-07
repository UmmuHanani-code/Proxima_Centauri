from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from models import db
import os


from models import db
from views.user_view import UserResourceView
from views.group_view import GroupResourceView
from views.project_view import ProjectResourceView
from views.qard_view import QardResourceView
from views.vote_view import VoteResourceView


app = Flask(__name__)
api = Api(app)


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "project.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'proxima-centauri-secret'
app.json.compact = False


db.init_app(app)
migrate = Migrate(app, db)


api.add_resource(UserResourceView, '/api/users', '/api/users/<int:user_id>')
api.add_resource(GroupResourceView, '/api/groups', '/api/groups/<int:group_id>')
api.add_resource(ProjectResourceView, '/api/projects', '/api/projects/<int:project_id>')
api.add_resource(QardResourceView, '/api/qards', '/api/qards/<int:qard_id>')
api.add_resource(VoteResourceView, '/api/votes', '/api/votes/<int:vote_id>')


if __name__ == '__main__':
    app.run(debug=True)
