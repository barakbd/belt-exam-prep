from system.core.controller import *
from datetime import datetime

class Books(Controller):
    def __init__(self, action):
        super(Books, self).__init__(action)
        self.load_model('Book_Model')
        self.db = self._app.db

    def index(self):
        print 'Home page - session is ',session,'\n'
        # session.clear()
        key_exists=session.get('user_id')
        if not key_exists:
            return redirect ('/')
        else:
            latest_reviews=self.models['Book_Model'].latest_reviews()
            print 'Books - Latest 3 reviews are ', latest_reviews, '\n'

            all_books=self.models['Book_Model'].all_books()
            print 'Books - all books are ', all_books, '\n'

            return self.load_view('books.html', latest_reviews=latest_reviews, all_books=all_books)

    ######################## LINK TO ADD BOOK PAGE #############################################
    def add_book_page(self):
        return self.load_view('add_book.html')

    ######################## SHOW BOOKS #############################################

    def view_book(self, book_id):
        print 'Books - view_book ','\n'
        return self.load_view('view_book.html')
        pass

    def add_book_submit(self):
        print 'Books - add_book_submit ','\n'
        print 'Add book form is', request.form,'\n'
        new_book=self.models['Book_Model'].add_book_submit(request.form, session)
        if new_book['status'] == False:
            for error in new_book['errors']:
                flash(error, 'add_book_error')
                print 'flash messages: ',session['_flashes'],'\n'
            return redirect ('/books/add')
        else:
            book_add_success_message = request.form['book_title'], ' added succesfully!'
            print  book_add_success_message, '\n'
            flash(book_add_success_message, 'success')
            return redirect ('/books')
