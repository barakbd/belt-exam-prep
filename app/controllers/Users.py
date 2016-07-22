from system.core.controller import *
from datetime import datetime

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        # self.load_model('Registration_Model')
        self.db = self._app.db

    def view_user(self, id):
        return self.load('view_user.html')
