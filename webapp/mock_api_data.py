from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:8000"}})

# Define a mock API route
@app.route('/api/customers', methods=['GET'])
def mock_resource():
    return jsonify({
                "cust_id": 1, 
                "firstname": "John", 
                "lastname":"Doe", 
                "salary": 3333, 
                "amount": 100, 
                "percentage": 0.03 
            },
            {
                "cust_id": 2,
                "firstname": "Simon",
                "lastname": "Bollard",
                "salary": 5000,
                "amount": 150,
                "percentage": 0.03
            },
            {
                "cust_id": 3,
                "firstname": "Steven",
                "lastname": "Jones",
                "salary": 6000,
                "amount": 360,
                "percentage": 0.06
            },  )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)