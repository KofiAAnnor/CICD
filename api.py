from flask import Flask, request, jsonify, json
import mysql.connector
import boto3

# Initializing app and database
app = Flask(__name__)

genders = ['male', 'female', 'other']
years = ['freshman', 'sophmore', 'junior', 'senior']
'''
client = boto3.client('secretsmanager', region_name='us-east-2')
response = client.get_secret_value(
    SecretId = 'dbsecrets'
)

secretDict = json.loads(response['SecretString'])

mydb = mysql.connector.connect(
  host=secretDict['host'],
  user=secretDict['username'],
  password=secretDict['password'],
  database="studentdatabase"
)

mycursor = mydb.cursor()'''

def studentExists(uid):
    '''
    sql = "SELECT * FROM students WHERE uid = %s"
    val = (uid,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()
    if myresult:
        return True
    else:
        return False
    '''

# Serves GET and POST requests for API
@app.route("/", methods=['GET'])
def getHomePage():
    return "<h1>THIS IS A TEST API</h1>", 200

@app.route("/students", methods=['GET'])
def getAllStudents():
    return "<h1>GET STUDENTS</h1>", 200
    '''
    sql = "SELECT * FROM students"
    mycursor.execute(sql)

    row_headers = [x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    json_data = []

    for result in myresult:
        json_data.append(dict(zip(row_headers,result)))
        
    return jsonify(json_data), 200 '''

@app.route("/student/<uid>", methods=['GET'])
def getStudent(uid):
    return "<h1>GET STUDENT</h1>", 200
    '''if not studentExists(uid):
        return {}, 404

    sql = "SELECT * FROM students WHERE uid = %s"
    val = (uid, )
    mycursor.execute(sql, val)
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    myresult = mycursor.fetchall()
    json_data =[]
    for result in myresult:
        json_data.append(dict(zip(row_headers,result)))
    return jsonify(json_data[0]), 200'''

@app.route("/add", methods=['POST'])
def addStudent():
    return "<h1>ADD STUDENT</h1>", 200

    '''student = request.json
    uid = student['uid']
    name = student['name']
    gender = student['gender']
    gpa = student['gpa']
    year = student['year']
    if not studentExists(uid) and gender in genders and year in years:
        sql = "INSERT INTO students (uid, name, gender, gpa, year) VALUES (%s, %s, %s, %s, %s)"
        val = (uid, name, gender, gpa, year)
        mycursor.execute(sql, val)
        mydb.commit()
        return jsonify({'success':True}), 200
    else:
        return {}, 400'''

@app.route("/delete/<uid>", methods=['DELETE'])
def deleteStudent(uid):
    return "<h1>DELETE STUDENT</h1>", 200

    '''if  studentExists(uid):
        sql = "DELETE FROM students WHERE uid = %s"
        val = (uid, )
        mycursor.execute(sql, val)        
        mydb.commit()
        return jsonify({'success':True}), 200
    else:
        return {} , 404'''
        

# Running application
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
