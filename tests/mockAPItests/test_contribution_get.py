import unittest
from sample_customer_data import TestData

from unittest.mock import Mock, patch, MagicMock

class GetCustomerData(unittest.TestCase):
    @patch('requests.get')
    def test_get_user_data(self, mock_response):
        
        mock_response = MagicMock()

        mock_response.json.return_value = TestData.get_customers()[0] 

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