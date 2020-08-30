from flask import Flask, request, jsonify

# Initializing app and database
app = Flask(__name__)
database = {}

# Serves GET and POST requests for API
@app.route("/", methods=['GET', 'POST'])
def index():
    return jsonify(database)

# Running application
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
