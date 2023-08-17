import json

class TestData:
    def get_customers():
        list_of_customers = [ 
            {
                "cust_id": 1, 
                "firstname": "John", 
                "lastname":"Doee", 
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
                "firstname": "Simon",
                "lastname": "Bollard",
                "salary": 6000,
                "amount": 360,
                "percentage": 0.06
            },  
        ]  
    
        json_customers = json.dumps(list_of_customers)
        return list_of_customers
    

