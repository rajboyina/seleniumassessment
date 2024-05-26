import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from locators import Locators

#Chrome Driver initialization
@pytest.fixture(scope="module")
def driver():
    # Initialize WebDriver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

#Registration Test Case
@pytest.mark.registration
def test_registration(driver):
    # Open the Demoblaze website
    driver.get('https://www.demoblaze.com/')

    # Wait for the page to load
    wait = WebDriverWait(driver, 10)

    # Click on the Sign up button
    sign_up_button = wait.until(EC.element_to_be_clickable(Locators.SIGN_UP_BUTTON))
    sign_up_button.click()

    # Wait for the Sign up modal to appear
    wait.until(EC.visibility_of_element_located(Locators.SIGN_UP_MODAL))

    # Fill in the registration details
    username = 'testuser12387619'  # replace with desired username
    password = 'test123'           # replace with desired password

    # Find the username and password input fields
    username_input = driver.find_element(*Locators.SIGN_UP_USERNAME_INPUT)
    password_input = driver.find_element(*Locators.SIGN_UP_PASSWORD_INPUT)

    # Enter the username and password
    username_input.send_keys(username)
    password_input.send_keys(password)

    # Click the Sign up button in the modal
    signup_modal_button = driver.find_element(*Locators.SIGN_UP_MODAL_BUTTON)
    signup_modal_button.click()

    # Wait for some time to let the registration process complete
    time.sleep(5)

    # Checking for an alert message after registration successful
    alert = wait.until(EC.alert_is_present())
    alert_text = alert.text
    assert 'Sign up successful.' in alert_text

    # Accept the alert to close it
    alert.accept()

#Login Test Case
@pytest.mark.login
def test_login(driver):
    # Open the Demoblaze website
    driver.get('https://www.demoblaze.com/')

    # Wait for the page to load
    wait = WebDriverWait(driver, 10)

    # Click on the Log in button
    login_button = wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
    login_button.click()

    # Wait for the Log in modal to appear
    wait.until(EC.visibility_of_element_located(Locators.LOG_IN_MODAL))

    # Fill in the login details
    username = 'test123876'  #replace with actual username
    password = 'test123'     #replace with actual password

    # Find the username and password input fields
    username_input = driver.find_element(*Locators.LOGIN_USERNAME_INPUT)
    password_input = driver.find_element(*Locators.LOGIN_PASSWORD_INPUT)

    # Enter the username and password
    username_input.send_keys(username)
    password_input.send_keys(password)

     # Click the Log in button in the modal
    login_modal_button = driver.find_element(*Locators.LOGIN_MODAL_BUTTON)
    login_modal_button.click()

    # Wait for some time to let the login process complete
    time.sleep(5)

    # Verify the login was successful and check if the username is displayed in the navbar
    welcome_user = wait.until(EC.visibility_of_element_located(Locators.WELCOME_USER))
    assert 'Welcome test123876' in welcome_user.text

#Product Search Test Case
@pytest.mark.productSearch
def test_product_search(driver):
    # Open the Demoblaze website
    driver.get('https://www.demoblaze.com/')

    # Wait for the page to load
    wait = WebDriverWait(driver, 10)

    # Search for a product
    product_name = 'Samsung galaxy s6'  # replace with the desired product name

    # Find the product link and click on it
    product_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, product_name)))
    product_link.click()

    # Wait for the product details page to load
    wait.until(EC.visibility_of_element_located(Locators.PRODUCT_NAME))

    # Verify the product details page is displayed
    product_title = driver.find_element(*Locators.PRODUCT_NAME).text
    assert product_name in product_title

    # Optionally, you can add more verifications like price, description, etc.
    product_price = driver.find_element(*Locators.PRODUCT_PRICE).text
    print(f'Product Name: {product_title}')
    print(f'Product Price: {product_price}')

#Add to Cart Test Case
@pytest.mark.addToCart
def test_add_to_cart(driver):
    # Open the Demoblaze website
    driver.get('https://www.demoblaze.com/')

    # Wait for the page to load
    wait = WebDriverWait(driver, 10)

    # Search for a product
    product_name = 'Samsung galaxy s6'  # replace with the desired product

    # Find the product link and click on it
    product_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, product_name)))
    product_link.click()

    # Wait for the product details page to load
    wait.until(EC.visibility_of_element_located(Locators.PRODUCT_NAME))

     # Click the "Add to Cart" button
    add_to_cart_button = driver.find_element(*Locators.ADD_TO_CART_BUTTON)
    add_to_cart_button.click()

    # Wait for the alert and accept it
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    # Optionally, verify that the product is added to the cart by navigating to the cart page
    cart_link = driver.find_element(*Locators.CART_LINK)
    cart_link.click()

     # Wait for the cart page to load and verify the product is in the cart
    wait.until(EC.visibility_of_element_located(Locators.CART_ITEM_NAMES))
    cart_items = driver.find_elements(*Locators.CART_ITEM_NAMES)
    cart_product_names = [item.text for item in cart_items]
    assert product_name in cart_product_names

    # Print cart items for verification
    print(f'Products in cart: {cart_product_names}')

def add_product_to_cart(driver, product_name):
    # Wait for the page to load
    wait = WebDriverWait(driver, 10)

    # Find the product link and click on it
    product_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, product_name)))
    product_link.click()

    # Wait for the product details page to load
    wait.until(EC.visibility_of_element_located(Locators.PRODUCT_NAME))

    # Click the "Add to Cart" button
    add_to_cart_button = driver.find_element(*Locators.ADD_TO_CART_BUTTON)
    add_to_cart_button.click()

    # Wait for the alert and accept it
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    # Go back to home page to add another product if needed
    home_link = driver.find_element(*Locators.HOME_LINK)
    home_link.click()

#Checout Test Case
@pytest.mark.checkout
def test_checkout(driver):
    # Wait for the page to load
    driver.get('https://www.demoblaze.com/')

    # Add a product to the cart
    product_name = 'Samsung galaxy s6'
    add_product_to_cart(driver, product_name)

    # Navigate to the cart page
    cart_link = driver.find_element(*Locators.CART_LINK)
    cart_link.click()

    # Wait for the cart page to load
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(Locators.CART_ITEM_NAMES))

    # Click on the "Place Order" button
    place_order_button = driver.find_element(*Locators.PLACE_ORDER_BUTTON)
    place_order_button.click()

    # Wait for the place order modal to appear
    wait.until(EC.visibility_of_element_located(Locators.ORDER_MODAL))

    # Fill in the order details
    name = 'Test User'
    country = 'USA'
    city = 'New York'
    credit_card = '1234567890123456'
    month = '12'
    year = '2024'

    driver.find_element(By.ID, 'name').send_keys(name)
    driver.find_element(By.ID, 'country').send_keys(country)
    driver.find_element(By.ID, 'city').send_keys(city)
    driver.find_element(By.ID, 'card').send_keys(credit_card)
    driver.find_element(By.ID, 'month').send_keys(month)
    driver.find_element(By.ID, 'year').send_keys(year)

    # Click on the "Purchase" button
    purchase_button = driver.find_element(*Locators.PURCHASE_BUTTON)
    purchase_button.click()

    # Wait for the purchase confirmation modal
    # wait.until(EC.visibility_of_element_located(*Locators.CONFIRMATION_MODAL))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.sweet-alert')))


    # Verify the purchase was successful
    confirmation_message = driver.find_element(*Locators.CONFIRMATION_MESSAGE).text
    assert 'Thank you for your purchase!' in confirmation_message

    # Print the purchase details for verification
    purchase_details = driver.find_element(*Locators.PURCHASE_DETAILS).text
    print(f'Purchase Confirmation: {confirmation_message}')
    print(f'Purchase Details: {purchase_details}')

    # Click on the "OK" button to close the confirmation modal
    ok_button = driver.find_element(*Locators.CONFIRM_BUTTON)
    ok_button.click()