import json
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver_fixture():
    chrome_options = Options()
    # Initialize the WebDriver
    driver = webdriver.Chrome(service=Service (ChromeDriverManager().install()), options=chrome_options)
    yield driver
    driver.quit()   

class TestTableData:
    def test_table_data_matches_json(self, driver_fixture):
     
        # Load JSON data from the provided data
        json_data = [
            {"amount": 100, "cust_id": 1, "firstname": "John", "lastname": "Doe", "percentage": 0.03, "salary": 3333},
            {"amount": 150, "cust_id": 2, "firstname": "Simon", "lastname": "Bollard", "percentage": 0.03, "salary": 5000},
            {"amount": 360, "cust_id": 3, "firstname": "Steven", "lastname": "Jones", "percentage": 0.06, "salary": 6000}
        ]

        # Open the URL
        url = "http://localhost:8000"
        driver_fixture.get(url)
        driver_fixture.maximize_window()

        #wait for table need a better solution than a static wait
        WebDriverWait(driver_fixture, 1000)

        # Find the table element
        table = driver_fixture.find_element(By.TAG_NAME,'table')

        # Find all table rows
        rows = table.find_elements(By.TAG_NAME,'tr')[1:]

        for row, json_entry in zip(rows, json_data):
            columns = row.find_element(By.TAG_NAME,'td')

            # Compare each column value with JSON data
            assert int(columns[0].text) == json_entry["amount"]
            assert int(columns[1].text) == json_entry["cust_id"]
            assert columns[2].text == json_entry["firstname"]
            assert columns[3].text == json_entry["lastname"]
            assert float(columns[4].text) == json_entry["percentage"]
            assert int(columns[5].text) == json_entry["salary"]

if __name__ == '__main__':
    pytest.main()
