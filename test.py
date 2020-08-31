from api import app
import unittest
from flask import json
import logging



class Tests(unittest.TestCase):

    def test_add(self):
        tester = app.test_client(self)
        response = tester.get('/students', content_type='html/text')
        print(resonce)
        #self.assertEqual(response.status_code, 200)

#        tester = app.test_client(self)
 #       self.assertEqual(400, 400)

if __name__ == "__main__":
    unittest.main()
