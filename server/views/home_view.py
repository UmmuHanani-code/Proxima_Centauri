
from flask_restful import Resource
from controllers.home_controller import HomeController

class HomeResourceView(Resource):
    def get(self):
        return HomeController.homepage()