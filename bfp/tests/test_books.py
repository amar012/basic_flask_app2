import os
import unittest
from bfp import app, db

TEST_DB = 'test.db'

class ProjectTests(unittest.TestCase):
    
    def setUp(self):
        app.config['DEBUG'] = False
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.config['BASEDIR'], TEST_DB)
        self.app = app.test_client()

        db.create_all()

        self.assertEquals(app.config['DEBUG'], False)
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_home_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b'List of Books', response.data)

    def test_home_page_query_results(self):
        response = self.app.get('/add', follow_redirects=True)
        self.assertIn(b'Add a New Book', response.data)

    #def test_add_book(self):
        #response = self.app.post('/add', data=dict(book_title='Test Book', book_genre='Testing'), follow_redirects=True)
        #self.assertIn(b'New book, Test Book, added!', response.data)

    #def test_add_invalid_book(self):
        #response = self.app.post('/add', data=dict(book_title='', book_genre='Testing for invalid book'), follow_redirects=True)
        #self.assertIn(b'ERROR! Book was not added', response.data)
        #self.assertIn(b'This field is required.', response.data)

if __name__ == '__main__':
    unittest.main() 