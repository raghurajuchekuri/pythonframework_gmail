import time

from core.resources.resource import GenericResource
from core.runtime import connection_manager
from core.lib.browser import WebCore


class Website(GenericResource):
    """This resource class is meant to represent a website endpoint.
    The following attributes are mandatory and must be passed via the testbed yml file.

    attributes:
        :ip: URL or IP Address of Website
        :version: Version number of website in string format. You can just pass 1.0 if no such version exists.
    """

    def __init__(self, resource_info):
        super(Website, self).__init__(resource_info)
        self.browser = None
        self.options = None
        self.capabilities = None

    def bootstrap(self):
        """Sets version for website. Purely to provide uniform interface as other resources do."""
        ## TODO open browser window should work independently
        self.connected = True

    def open_browser_window(self, browser="Chrome", options=None, conn_name="default", capabilities=None,
                            remote_server=None):
        """This method opens a browser window of desired type. The name attribute is used to name instances of browsers.
        This is used in conjunction with browser attribute to register a "connection" with the conn_manager.

        The behavior is that if no name is mentioned, then every actor calling this method would get the same browser
        window. If user wants a different window, or to retrieve another browser, the name must be supplied.

        args:
            :browser (str): The browser to be used for testing. Chrome(Default)|Firefox.
            :options: A webdriver.ChromeOptions or webdriver.FirefoxProfile object.
            :name: Name of the browser instance. Default - "default"
            :capabilities: Dictionary where user can specify the browser, version, vnc options, etc.
            :remote_server: Remote server details where selenium drivers are located
        """
        self.browser = browser
        self.options = options
        self.capabilities = capabilities
        self.driver = connection_manager.get(WebCore, browser=browser, options=options, name=conn_name,
                                             capabilities=capabilities, remote_server=remote_server)

    def restart_driver(self):
        """Restart the browser and navigate to the same url
        """
        curr_url = self.driver.webdriver.current_url
        self.driver.quit()
        del self.driver
        time.sleep(2)
        self.driver = WebCore(self.browser, self.options)
        self.driver.goto_address(curr_url)

    def quit(self):
        """This method will close the browser window, and remove the corresponding entry from conn manager.
        """
        connection_manager.remove(WebCore, self.browser, self.driver.name)
        self.driver.quit()

    def screenshot(self, file_name):
        """This method will save screenshot.

            args:
                :file_name str: Name of screenshot, .png file.
       """
        self.driver.save_screenshot(file_name=file_name)
