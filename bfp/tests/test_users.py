import unittest
from bfp import app

class ProjectTests(unittest.TestCase):
    
    def setUp(self):
        app.config['DEBUG'] = False
        app.config['TESTING'] = True
        self.app = app.test_client()

        self.assertEquals(app.config['DEBUG'], False)
    
    def tearDown(self):
        pass

    def test_home_page(self):
        response = self.app.get('/login', follow_redirects=True)
        self.assertIn(b'Log In', response.data)
    
if __name__ == '__main__':
    unittest.main() 