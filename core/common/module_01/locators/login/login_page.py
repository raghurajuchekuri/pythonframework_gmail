from selenium.webdriver.common.by import By


class SampleLogin:

    USERNAME = By.ID, 'email'
    PASSWORD = By.ID, 'password'
    LOGIN_BUTTON = By.ID, 'Login'
    DASHBOARD = By.ID, 'page-title'
