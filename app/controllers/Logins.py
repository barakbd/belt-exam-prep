from system.core.controller import *
from datetime import datetime

class Logins(Controller):
    def __init__(self, action):
        super(Logins, self).__init__(action)
        self.load_model('Login_Model')
        self.db = self._app.db

    def login(self):
        login_status = self.models['Login_Model'].login(request.form)
        if login_status['status'] == False:
            for message in login_status['errors']:
                flash(message, 'login_error')
                print 'flash messages: ',session['_flashes'],'\n'
            return redirect ('/')
        else:
            user_details = login_status['user_details'][0]
            print 'User details are ',user_details,'\n'
            session['user_id'] = user_details['user_id']
            session['first_name'] = user_details['first_name']

            return redirect ('/')

    ######################## RESET #############################################
    def reset_password_submit(self):
        return redirect('/')
