from system.core.model import Model

class User_Model(Model):
    def __init__(self):
        super(User_Model, self).__init__()

    def view_user(self, form):
        return self.load_view('view_user.html')
