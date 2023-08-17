# Pension Contribution Tests

This is an Automation Test suite for the purpose of verifying the API functionality for the Pension Contribution API. This suite uses mocking for validation, and also a stub server. The allure report is utlised to provide the results.

## Features

-- **Mocking API Interaction**: Testing the code is interacting with the api return values as expected
-- **Stub for API Interaction**: Test the endpoint of the pension contribution using a stub server on http://locahost:8000

## Installation and Usage

1. Install Python and pip on your system if they are not already installed.
2. Clone this repository: `git clone https://github.com/QualityAutomationTester/PensionContributionTests.git`
3. Navigate to the project directory: `cd pension-contribution-api-tests`
4. Install required dependencies: `pip install -r requirements.txt`
6. Run the tests and generate the report `pytest --alluredir=allure-results`
7. Generate the report with allure `allure generate allure-results --clean -o allure-report`
8. then `allure serve`
