import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)

# MySQL database configuration
app.config['MYSQL_HOST'] = 'your_mysql_host'
app.config['MYSQL_USER'] = 'your_mysql_username'
app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
app.config['MYSQL_DB'] = 'your_mysql_database_name'

# Establish MySQL connection
connection = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)
# You can create a separate config.py file to store these sensitive settings securely.
# Helper function to get the MySQL connection
def get_db_connection():
    return connection

# Add code here to configure your MySQL connection

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_prescription():
    if request.method == 'POST':
        # Aceess form data
        patient_name = request.form['patient_name']
        age = request.form['age']
        gender = request.form['gender']
        # Add  code  to acces othe form fields
        lab_report_file = request.files['lab_report']
        cursor = connection.cursor()
        return 'Prescription submitted successfully!'
    return 'Invalid request method'
    
if __name__ == '__main__':
    app.run(debug=True)
