from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

from selenium.common.exceptions import NoSuchElementException
import core


class CpanelLogin:
    """This class allows to login into the CPANEL with credentials"""
    TIME_SEC = 5

    def __init__(self, host):

        self.driver = core.get(core.res['chrome'], feature="browser")._res.driver.webdriver
        self.host = host
        self.access_login_page()

    def access_login_page(self):
        """Method to get the current URL

        returns:
          URL as a String object if exist
        """

        self.driver.get(f"{self.host}/module_01/")

