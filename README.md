# Hybrid_Automation_Framework



SauceDemo Automation Framework
==============================

This project is an end-to-end automation framework built with Python, Pytest, Selenium, PostgreSQL, and Allure Reports.  
It automates the login, inventory, add-to-cart, and checkout process on the SauceDemo application.

---------------------------------
Features
---------------------------------
- Pytest Framework – test execution & reporting
- Selenium WebDriver – browser automation
- Page Object Model (POM) – clean, maintainable code
- Database Integration (PostgreSQL) – fetch user credentials & checkout data directly from DB
- Parameterized Tests – run tests with multiple users
- Allure Reporting – beautiful, interactive test reports
- Logging – track test execution & errors
- Test Ordering – define execution sequence with pytest-order

---------------------------------
Setup & Installation
---------------------------------
1. Clone the Repository
   git clone https://github.com/your-username/Hybrid_Automation_Framework.git

2. Create & Activate Virtual Environment
   python3 -m venv .venv
   source .venv/bin/activate   (Mac/Linux)
   .venv\Scripts\activate      (Windows)

3. Install Dependencies
   pip install -r requirements.txt

4. Configure Database (PostgreSQL)
   Create tables & insert dummy data:

   CREATE TABLE users (
       id SERIAL PRIMARY KEY,
       username VARCHAR(50),
       password VARCHAR(50),
       is_valid BOOLEAN
   );

   CREATE TABLE addresses (
       id SERIAL PRIMARY KEY,
       first_name VARCHAR(50),
       last_name VARCHAR(50),
       zipcode VARCHAR(10)
   );

   INSERT INTO users (username, password, is_valid)
   VALUES ('standard_user', 'secret_sauce', TRUE);

   INSERT INTO addresses (first_name, last_name, zipcode)
   VALUES ('John', 'Doe', '12345');

   Update your DB connection in utility/db_connection.py.

---------------------------------
Running Tests
---------------------------------
Run All Tests:
   pytest -v

Run with Allure Reporting:
   pytest --alluredir=reports/
   allure serve reports/

Run with Test Ordering:
   pytest --order-scope=class

---------------------------------
Allure Reports
---------------------------------
After execution:
   allure serve reports/
This opens an interactive report in your browser.

---------------------------------
Logging
---------------------------------
Logs are generated automatically in the logs/ folder:
logs/test_log_YYYY-MM-DD_HH-MM-SS.log

---------------------------------
Example Test Flow
---------------------------------
1. Login using credentials from DB
2. Inventory Page – fetch & verify product list
3. Add to Cart – add selected items
4. Checkout – fill address from DB
5. Verify Order – ensure success message is displayed

---------------------------------
Tech Stack
---------------------------------
- Python 3.10+
- Pytest
- Selenium
- PostgreSQL
- Allure
- Logging

---------------------------------
Future Improvements
---------------------------------
- Integrate CI/CD (GitHub Actions / Jenkins)
- Dockerize the framework

---------------------------------
Author
---------------------------------
Developed by Ujjawal Kumar
