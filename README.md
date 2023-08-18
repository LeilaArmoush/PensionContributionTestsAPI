# Pension Contribution Tests

This is an Automation Test suite for the purpose of verifying the API functionality for the Pension Contribution API. This suite uses mocking for validation, and also a stub server. The allure report is utlised to provide the results.

## Features

-- **Mocking API Interaction**: Testing the code is interacting with the api return values as expected


-- **Stub for API Interaction**: Test the endpoint of the pension contribution using a stub server


-- **UI tests**: Test that the user interface is displaying the pension contributions on a web application

## Installation and Usage

1. Install Python and pip on your system if they are not already installed.
2. Clone this repository: `git clone https://github.com/QualityAutomationTester/PensionContributionTests.git`
3. Navigate to the project directory: `cd pension-contribution-api-tests`
4. Install required dependencies: `pip install -r requirements.txt`
5. Start the API stub by navigating into the webapp folder and running `python mock_api_data.py` this will be hosted on port 5000
6. Start the frontend webapp by navigating into the webapp folder and running `python -m http.server` this will be hosted on port 8000 
7. Run the tests and generate the report `pytest --alluredir=allure-results`
8. Generate the report with allure `allure generate allure-results --clean -o allure-report`
9. then `allure serve`

## Pending Features ##

-- Appium tests to test that the pension contributions are being displayed correctly on the mobile application


-- Dockerisation of web application either using a windows container, configuring the requirements for a linux machine


-- jenkins pipeline build a jenkins pipeline that is triggered either when there is a change to the code or when a merge request is raised
