from system.core.model import Model

class Book_Model(Model):
    def __init__(self):
        super(Book_Model, self).__init__()

    def latest_reviews(self):
        latest_reviews=self.db.query_db('SELECT * FROM reviews LEFT JOIN books ON book_id=books_book_id LEFT JOIN users ON books.users_user_id = users.user_id ORDER BY reviews.created_at DESC LIMIT 3')
        print 'Books_Model - Latest 3 reviews are ', latest_reviews, '\n'
        return latest_reviews

    def all_books(self):
        all_books = self.db.query_db('SELECT * FROM books')
        return all_books

    def add_book_submit(self, form, session):
        print 'Book_Model - add_book_submit ','\n'
        errors=[]
        if not form['book_title'] or not form['review_text'] or not form['review_rating'] and (not form['select_author'] or not form['add_author']):
            errors.append('All fields are required')
        if (form['select_author'] and form['add_author']):
            errors.append('Select only 1 option for author')
            print 'Add book errors -', errors
            return {'status':False, 'errors':errors}


        data_add_book = {
                    'user_id': session['user_id'],
                    'book_title': form['book_title'],
                    'author_id': form['select_author'],
                    'add_author': form['add_author'],
                    'review_text': form['review_text'],
                    'review_rating': form['review_rating'],
                    'book_id': 1
                    }
        query_insert_book = 'INSERT INTO books (book_title, created_at, updated_at, authors_author_id, users_user_id) VALUES (:book_title, NOW(), NOW(), :author_id, :user_id)'

        if form['add_author']:
            query_add_author='INSERT INTO authors (author_name, created_at, updated_at) VALUES (:add_author, NOW(), NOW() )'
            new_author_id=self.db.query_db(query_add_author, data_add_book)

            data_add_book['author_id'] = new_author_id
            new_book_id=self.db.query_db(query_insert_book, data_add_book)
        else:
            new_book_id=self.db.query_db(query_insert_book, data_add_book)

        data_add_book['book_id'] = new_book_id
        query_insert_review = 'INSERT INTO reviews (review_rating, review_text, created_at, updated_at, books_book_id, books_authors_author_id, users_user_id) VALUES (:review_rating, :review_text, NOW(), NOW(), :book_id, :author_id, :user_id)'
        self.db.query_db(query_insert_review, data_add_book)

        return {'status': True, 'new_book_id': new_book_id}

    def view_book(self, book_id):
        query_view_book = 'SELECT *, (SELECT ROUND(AVG(review_rating),1) FROM reviews where books_book_id = :book_id) AS rating_avg FROM books LEFT JOIN reviews ON books_book_id = book_id LEFT JOIN authors ON authors_author_id = author_id LEFT JOIN users ON books.users_user_id = user_id WHERE book_id = :book_id'
        data_view_book = {'book_id' : book_id}
        book_details = self.db.query_db(query_view_book, data_view_book)
        print 'Book Model view_book', book_details, '\n'
        return book_details

    def add_review(self, book_id, form, session):
        data_add_review = {
                        'user_id': session['user_id'],
                        'review_text': form['review_text'],
                        'review_rating': form['review_rating'],
                        'book_id': book_id
                        }

        query_add_review = 'INSERT INTO reviews (review_rating, review_text, created_at, updated_at, books_book_id, users_user_id) VALUES (:review_rating, :review_text, NOW(), NOW(), :book_id, :user_id)'
        return self.db.query_db(query_add_review, data_add_review)
