import requests
import unittest

class GetCustomerData(unittest.TestCase):
    def test_get_customer_data_from_server(self):
        api_url = "http://localhost:5000/api/customers"
        response = requests.get(api_url)
        
        expected_data = {
            "cust_id": 1,
            "firstname": "John",
            "lastname": "Doe",
            "salary": 3333,
            "amount": 100,
            "percentage": 0.03
        }
        
        self.assertEqual( response.json()[0], expected_data)

if __name__ == "__main__":
     unittest.main()
