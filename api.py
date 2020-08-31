from flask import Flask, request, jsonify

# Initializing app and database
app = Flask(__name__)
database = {}
genders = ['male', 'female', 'other']
years = ['freshman', 'sophmore', 'junior', 'senior']

# Serves GET and POST requests for API
@app.route("/students", methods=['GET'])
def getAllStudents():
    return jsonify(database), 200

@app.route("/student/<uid>", methods=['GET'])
def getStudent(uid):
    student = database.get(uid)
    if student is None:
        return {}, 404
    else:
        return jsonify(database[uid]), 200

@app.route("/add", methods=['POST'])
def addStudent():
    student = request.json
    uid = student['uid']
    name = student['name']
    gender = student['gender']
    gpa = student['gpa']
    year = student['year']
    if database.get(uid) is None and gender in genders and year in years:
        studentEntry = {"uid": uid, "name": name, "gender": gender, "gpa": gpa, "year" : year}
        database[uid] = studentEntry
        status_code = flask.Response(status=200)
	    return status_code
    else:
        status_code = flask.Response(status=400)
	    return status_code
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
