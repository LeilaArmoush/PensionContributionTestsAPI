import unittest

from unittest.mock import patch, MagicMock

class GetCustomerData(unittest.TestCase):
    @patch('requests.get')
    def get_customers(self, ):
        return  
    
    def test_get_user_data(self):

        customers =   [ 
            {
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
                "firstname": "Simon",
                "lastname": "Bollard",
                "salary": 6000,
                "amount": 360,
                "percentage": 0.06
            },  
        ]  
        
        mock_response = MagicMock()

        mock_response.json.return_value = customers[0]

        expected_data = {
             "cust_id": 1,
            "firstname": "John",
            "lastname": "Doe",
            "salary": 3333,
            "amount": 100,
            "percentage": 0.03
        }
        
        self.assertEqual(mock_response.json(), expected_data)

if __name__ == "__main__":
     unittest.main()