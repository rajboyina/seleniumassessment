#This file contains all the locators information of the website

from selenium.webdriver.common.by import By

class Locators:
    # Home Page
    SIGN_UP_BUTTON = (By.ID, 'signin2')
    LOGIN_BUTTON = (By.ID, 'login2')
    HOME_LINK = (By.XPATH, '//*[@id="navbarExample"]/ul/li[1]/a')
    CART_LINK = (By.ID, 'cartur')

    # Sign Up Modal
    SIGN_UP_MODAL = (By.ID, 'signInModal')
    SIGN_UP_USERNAME_INPUT = (By.ID, 'sign-username')
    SIGN_UP_PASSWORD_INPUT = (By.ID, 'sign-password')
    SIGN_UP_MODAL_BUTTON = (By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]')

    # Log In Modal
    LOG_IN_MODAL = (By.ID, 'logInModal')
    LOGIN_USERNAME_INPUT = (By.ID, 'loginusername')
    LOGIN_PASSWORD_INPUT = (By.ID, 'loginpassword')
    LOGIN_MODAL_BUTTON = (By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    WELCOME_USER = (By.ID, 'nameofuser')

    # Product Page
    PRODUCT_NAME = (By.CSS_SELECTOR, '.name')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.price-container')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn-success')

    # Cart Page
    CART_ITEM_NAMES = (By.XPATH, '//tr/td[2]')
    PLACE_ORDER_BUTTON = (By.CSS_SELECTOR, '.btn-success')

    # Place Order Modal
    ORDER_MODAL = (By.ID, 'orderModal')
    ORDER_NAME_INPUT = (By.ID, 'name')
    ORDER_COUNTRY_INPUT = (By.ID, 'country')
    ORDER_CITY_INPUT = (By.ID, 'city')
    ORDER_CARD_INPUT = (By.ID, 'card')
    ORDER_MONTH_INPUT = (By.ID, 'month')
    ORDER_YEAR_INPUT = (By.ID, 'year')
    PURCHASE_BUTTON = (By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2]')
    CONFIRMATION_MESSAGE = (By.CSS_SELECTOR, '.sweet-alert h2')
    PURCHASE_DETAILS = (By.CSS_SELECTOR, '.sweet-alert p')
    CONFIRM_BUTTON = (By.CSS_SELECTOR, '.confirm')