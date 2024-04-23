# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Good To Have You Here..!!!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

