"""This module contains the new Selenium wrapper class which essentially serves as the driver for all Web UI testing and
provides helpful methods that make working with Selnium easier.
"""
import os
import datetime
import logging
import core

from selenium import webdriver
from selenium.common.exceptions import TimeoutException

CURRENT_CONFIG = {}

DEFAULT_TIMEOUT = 30


class WebCoreException(Exception):
    """Implements the FeatureException that can be used loosely when a WebCore function fails.
    """
    pass


class WebCore:
    """The Selenium wrapper class that contains many methods to make Web UI traversal and testing easy."""

    def __init__(self, browser="Chrome", options=None, name="default", remote_server=None, capabilities=None):
        """Init method for WebCore

        kwargs:
            :browser (str): The browser to be used for testing. Chrome(Default)|Firefox.
            :options: A webdriver.ChromeOptions or webdriver.FirefoxProfile object
            :name: Name of the browser instance.
            :capabilities: Dictionary where user can specify the browser, version, vnc options, etc.
            :remote_server: Remote server details where selenium drivers are located
        """
        self.currentpage = ""
        self.name = name

        # TODO better logdir and save screenshots in this dir
        log_dir = os.getcwd()
        self.download_dir = os.path.join(log_dir, "tmp", datetime.datetime.now().strftime("%d-%m-%Y@%H_%M"))
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)

        if browser.lower() == "chrome":
            service_log = os.path.join(log_dir, "tmp", "chrome.log")

            # TODO make sure service log doesn't exist
            if not options:
                options = webdriver.ChromeOptions()

            prefs = {"download.default_directory": self.download_dir}
            options.add_experimental_option("prefs", prefs)

            if remote_server:
                self.webdriver = webdriver.Remote(command_executor=remote_server)
            else:
                self.webdriver = webdriver.Chrome(service_log_path=service_log, chrome_options=options)
        elif browser.lower() == "firefox":
            service_log = os.path.join(log_dir, "tmp", "firefox.log")
            # TODO make sure service log doesn't exist
            if not options:
                options = webdriver.FirefoxProfile()
            options.set_preference("browser.download.dir", self.download_dir)
            options.set_preference("webdriver.log.file", service_log)

            if remote_server:
                self.webdriver = webdriver.Remote(command_executor=remote_server, desired_capabilities=capabilities)
            else:
                self.webdriver = webdriver.Firefox(firefox_profile=options)
        else:
            raise ValueError(f"Browser {browser} is not supported")

        self.webdriver.implicitly_wait(DEFAULT_TIMEOUT)
        self.webdriver.maximize_window()

    def goto_address(self, address=" "):
        """Method to make the browser go to the specified address

        args:
            :address: Destination URL
        """
        self.webdriver.get(address)

    def save_screenshot(self, file_name):
        """Method to take screenshot

       args:
           :file_name str: Name of screenshot, .png file.
       """
        global CURRENT_CONFIG

        CURRENT_CONFIG = core.load_yaml()
        if 'screenshots_path' not in CURRENT_CONFIG:
            raise ValueError("Screenshots path not given in yaml config file")
        path = CURRENT_CONFIG['screenshots_path'] + file_name
        try:
            self.webdriver.save_screenshot(path)
        except Exception:
            logging.error("Could not take the screenshot and save it to path: {}".format(path))
            raise WebCoreException("Could not take the screenshot and save it to path: {}".format(path))

    def get_url(self):
        """Method to get the current URL

        returns:
            URL as a String object if exist
        """
        url = ""
        try:
            url = self.webdriver.current_url
        except TimeoutException as exp:
            logging.error("Could not get the current URL due to {}".format(exp))
            raise WebCoreException("Could not get the current URL due to {}".format(exp))
        return url

    def quit(self):
        """Method to quit the driver"""
        self.webdriver.quit()
