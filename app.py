import os 
from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Hello Karim and Accenture/Swisscom/Udemy CoP Devops: ' + os.environ.get('MESSAGE')

app.run(debug=True, host='0.0.0.0', port=8080)