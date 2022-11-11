from flask import Flask, jsonify,request
from os import getenv
from config import DevConfig,Config
print("Starting app".center(80,'-'))

app = Flask(__name__)
app.config.from_object(Config)
# app.config.from_pyfile('config2.py')
# Create dummy data 

record = [
        {
            "name":"Dheeraj",
            "age":25,
            "profession":"Doctor"
        },
          {
            "name":"Binay",
            "age":22,
            "profession":"Lawyer"
        },
          {
            "name":"Ajitosh",
            "age":35,
            "profession":"Developer"
        },
          {
            "name":"Meera",
            "age":30,
            "profession":"Analyst"
        }

        ]

        # HTTP Requests allowed 
        # 1. GET
        # 2. POST
        # 3. PUT
        # 4. DELETE
        # 5. PATCH

        # The GET Request http://127.0.0.1:5300/get/all

@app.route('/get/all',methods=['GET'])
def get_all():
    return jsonify(record),200
    
# Add data [ POST REQUEST]
@app.route('/add/<data>',methods=['POST','GET'])
def add_data(data):   # View Functions 
    d1 = request.get_json()
    print(d1)
    record.append(d1)
    return jsonify(record),200

if __name__ == '__main__':
    app.run()

