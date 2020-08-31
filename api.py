from flask import Flask, request, jsonify

# Initializing app and database
app = Flask(__name__)
database = {}
genders = ['male', 'female', 'other']
year = ['freshman', 'sophmore', 'junior', 'senior']

# Serves GET and POST requests for API
@app.route("/students", methods=['GET'])
def getAllStudents():
    return jsonify(database), 200

@app.route("/student/<uid>", methods=['GET'])
def getStudent(uid):
    student = database.get(uid)
    if student is None:
        return 404
    else:
        return jsonify(student), 200

@app.route("/add", methods=['POST'])
def addStudent():
    for student in request.json:
        if database.get(student['uid']) != None:
            return 400
    for student in request.json:
        uid = student['uid']
        name = student['name']
        gender = student['gender']
        gpa = student['gpa']
        studentEntry = {"uid": uid, "name": name, "gender": gender, "gpa": gpa}
        database[uid] = studentEntry
    return 200
"""
@app.route("/delete/<uid>", methods=['DELETE'])
def deleteStudent(uid):
    student = database.get(uid)
    if student is None:
        return 404
    else:
        return database.popitem(uid), 200

@app.route("/update/<uid>", methods=['PUT'])
def updateStudent(uid):
    return jsonify(database), 200
"""
# Running application
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
