import core
from selenium.webdriver.common.by import By


class HomePage:
    SEARCH = By.NAME, 'q'
    SUBMIT = By.NAME, 'btnK'
    RESULTS = By.ID, 'resultStats'

    def __init__(self):
        self.driver = core.get(core.res['chrome'], feature="browser")._res.driver.webdriver

    def navigate(self,host):
        self.driver.get(host)

    def search(self, text):
        self.driver.find_element(*HomePage.SEARCH).send_keys(text)
        self.driver.find_element(*HomePage.SUBMIT).click()

    def element_visible(self,elment):
        self.driver.visibility_of_element_located(*HomePage.RESULTS)