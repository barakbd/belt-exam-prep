
from system.core.router import routes

routes['default_controller'] = 'Registrations'

routes['POST']['/register'] = 'Registrations#register'

routes['POST']['/login'] = 'Logins#login'

routes['POST']['/reset_password'] = 'Logins#reset_password_submit'

routes['GET']['/clear_session'] = 'Registrations#clear_session'

routes['GET']['/books'] = 'Books#index'

routes['GET']['/books/add'] = 'Books#add_book_page'

routes['POST']['/books/add_submit'] = 'Books#add_book_submit'

routes['GET']['/books/<int:book_id>'] = 'Books#view_book'

routes['POST']['/books/add_review/<book_id>'] = 'Books#add_review'

routes['GET']['/users/<user_id>'] = 'Users#view_user'







"""
    You can add routes and specify their handlers as follows:

    routes['VERB']['/URL/GOES/HERE'] = 'Controller#method'

    Note the '#' symbol to specify the controller method to use.
    Note the preceding slash in the url.
    Note that the http verb must be specified in ALL CAPS.

    If the http verb is not provided pylot will assume that you want the 'GET' verb.

    You can also use route parameters by using the angled brackets like so:
    routes['PUT']['/users/<int:id>'] = 'users#update'

    Note that the parameter can have a specified type (int, string, float, path).
    If the type is not specified it will default to string

    Here is an example of the restful routes for users:

    routes['GET']['/users'] = 'users#index'
    routes['GET']['/users/new'] = 'users#new'
    routes['POST']['/users'] = 'users#create'
    routes['GET']['/users/<int:id>'] = 'users#show'
    routes['GET']['/users/<int:id>/edit' = 'users#edit'
    routes['PATCH']['/users/<int:id>'] = 'users#update'
    routes['DELETE']['/users/<int:id>'] = 'users#destroy'
"""
