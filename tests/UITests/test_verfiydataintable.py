import json
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Initialize the WebDriver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.quit()

def test_table_data_matches_json(driver):
    # Load JSON data from the provided data
    json_data = [
        {"amount": 100, "cust_id": 1, "firstname": "John", "lastname": "Doe", "percentage": 0.03, "salary": 3333},
        {"amount": 150, "cust_id": 2, "firstname": "Simon", "lastname": "Bollard", "percentage": 0.03, "salary": 5000},
        {"amount": 360, "cust_id": 3, "firstname": "Steven", "lastname": "Jones", "percentage": 0.06, "salary": 6000}
    ]

    # Open the URL
    url = "http://localhost:8000"  # Update with your actual URL
    driver.get(url)

    # Find the table element
    table = driver.find_element_by_tag_name('table')

    # Find all table rows
    rows = table.find_elements_by_tag_name('tr')[1:]  # Exclude header row

    assert len(rows) == len(json_data), "Number of table rows doesn't match JSON data"

    for row, json_entry in zip(rows, json_data):
        columns = row.find_elements_by_tag_name('td')
        assert len(columns) == 6, "Incorrect number of table columns"

        # Compare each column value with JSON data
        assert int(columns[0].text) == json_entry["amount"]
        assert int(columns[1].text) == json_entry["cust_id"]
        assert columns[2].text == json_entry["firstname"]
        assert columns[3].text == json_entry["lastname"]
        assert float(columns[4].text) == json_entry["percentage"]
        assert int(columns[5].text) == json_entry["salary"]

if __name__ == '__main__':
    pytest.main()