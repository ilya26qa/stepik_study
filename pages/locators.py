from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators():
    BTN_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    ITEM_NAME = (By.CSS_SELECTOR, 'h1')
    BASKET_COUNT = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    CONFIRM_ITEM_NAME = (By.CSS_SELECTOR, '#messages div:nth-child(1) strong')
    CONFIRM_BASKET_COUNT = (By.CSS_SELECTOR, '#messages div:nth-child(3) strong')


class LoginPageLocators():
    LOGIN_MAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REG_MAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTRATION_FORM = (By.ID, 'register_form')
