# Selenium Python Project with Pytest

This repository contains automated test scripts for the Demoblaze website using Python and Selenium with the pytest framework. The test cases include user registration, login, product search, adding products to the cart, and the checkout process.

# Prerequisites

Ensure you have the following installed on your machine:

    Python 3.x
    pip (Python package installer)
    Google Chrome (or another supported browser)
    ChromeDriver (or the appropriate WebDriver for your browser)

# Installation

Clone the repository:

git clone https://github.com/rajboyina/seleniumassessment.git
cd seleniumassessment

# Install the required Python packages:

    pip install -r requirements.txt

Test Cases are written in test_cases.py file

1. Registration Test

    function: test_registration()
    Description: Automates the user registration process on the Demoblaze website.

2. Login Test

    function: test_login()
    Description: Automates the user login process on the Demoblaze website.

3. Product Search Test

    function: test_product_search()
    Description: Automates the product search process on the Demoblaze website.

4. Add to Cart Test

    function: test_add_to_cart()
    Description: Automates the process of adding a product to the cart on the Demoblaze website.

5. Checkout Test

    function: test_checkout()
    Description: Automates the checkout process on the Demoblaze website.

# Running Tests

To run the tests, use the following command:

python -m pytest --html=report.html

This command will discover and run all the test cases in the project and generates html report of the test cases in report.html file .