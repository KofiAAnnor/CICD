from api import app
import unittest
from flask import json
import logging



class Tests(unittest.TestCase):

    def test_getAllStudents(self):
        tester = app.test_client(self)
        response = tester.get('/students', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {})
    
    def test_getStudent(self):
        tester = app.test_client(self)
        response = tester.get('/student/14654368', content_type='html/text')
        self.assertEqual(response.status_code, 400)

    def test_addStudent(self):
        tester = app.test_client(self)
        
        valid_js = {"uid": 1267893, "name": "James Gordon", "gender": "male", "gpa": 3.500, "year" : "senior"}
        invalid_js_1 = {"uid": 1267893, "name": "James Gordon", "gender": "male", "gpa": 3.500, "year" : "seniors"}
        invalid_js_2 = {"uid": 1267893, "name": "James Gordon", "gender": "males", "gpa": 3.500, "year" : "senior"}
        invalid_js_3 = {"uid": 1267893, "name": "James Cordon", "gender": "male", "gpa": 3.600, "year" : "senior"}
        
        valid_response = tester.post('/add', data=json.dumps(valid_js), content_type='application/json')
        invalid_1_response = tester.post('/add', data=json.dumps(invalid_js_1), content_type='application/json')
        invalid_2_response = tester.post('/add', data=json.dumps(invalid_js_2), content_type='application/json')
        invalid_3_response = tester.post('/add', data=json.dumps(invalid_js_3), content_type='application/json')
        
        self.assertEqual(responsevalid_response.status_code, 200)
        self.assertEqual(invalid_1_response.status_code, 400)
        self.assertEqual(invalid_2_response.status_code, 400)
        self.assertEqual(invalid_3_response.status_code, 400)

    def test_getAllStudents2(self):
        tester = app.test_client(self)
        response = tester.get('/students', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {1267893 : {"uid": 1267893, "name": "James Gordon", "gender": "male", "gpa": 3.500, "year" : "senior"}})

    def test_getStudent2(self):
        tester = app.test_client(self)
        response = tester.get('/student/1267893', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json,{"uid": 1267893, "name": "James Gordon", "gender": "male", "gpa": 3.500, "year" : "senior"})




#        tester = app.test_client(self)
 #       self.assertEqual(400, 400)

if __name__ == "__main__":
    unittest.main()
