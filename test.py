from api import app
import unittest
from flask import json, jsonify
import logging



class Tests(unittest.TestCase):
    
    def test_dbfunctionality(self):
        self.assertEqual(400, 400)
        tester = app.test_client(self)

        # test getStudent empty at first
        response = tester.get('/student/14654368', content_type='html/text')
        self.assertEqual(response.status_code, 404)
        
        # test valid and invalid add
        valid_js = {"uid": 1267893, "name": "James Gordon", "gender": "male", "gpa": 3.500, "year" : "senior"}
        invalid_js_1 = {"uid": 1267893, "name": "James Gordon", "gender": "male", "gpa": 3.500, "year" : "seniors"}
        invalid_js_2 = {"uid": 1267893, "name": "James Gordon", "gender": "males", "gpa": 3.500, "year" : "senior"}
        invalid_js_3 = {"uid": 1267893, "name": "James Cordon", "gender": "male", "gpa": 3.600, "year" : "senior"}
        
        valid_response = tester.post('/add', data=json.dumps(valid_js), content_type='application/json')
        invalid_1_response = tester.post('/add', data=json.dumps(invalid_js_1), content_type='application/json')
        invalid_2_response = tester.post('/add', data=json.dumps(invalid_js_2), content_type='application/json')
        invalid_3_response = tester.post('/add', data=json.dumps(invalid_js_3), content_type='application/json')
        
        self.assertEqual(valid_response.status_code, 200)
        self.assertEqual(invalid_1_response.status_code, 400)
        self.assertEqual(invalid_2_response.status_code, 400)
        self.assertEqual(invalid_3_response.status_code, 400)

        # test getStudent 
        response = tester.get('/student/1267893', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"uid": 1267893, "name": "James Gordon", "gender": "male", "gpa": 3.500, "year" : "senior"})
    
        # test deleteStudent 
        response = tester.delete('/delete/12676786', content_type='html/text')
        self.assertEqual(response.status_code, 404) 

        response = tester.delete('/delete/1267893', content_type='html/text')
        self.assertEqual(response.status_code, 200)

        # test getStudent empty
        response = tester.get('/student/1267893', content_type='html/text')
        self.assertEqual(response.status_code, 404)
    
if __name__ == "__main__":
    unittest.main()
