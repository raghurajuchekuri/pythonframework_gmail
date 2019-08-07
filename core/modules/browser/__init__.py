from core.modules import GenericFeature


class Browser(GenericFeature):
    """Browser defines the interface to execute actions on a host running selenium.
    """
    def get_address(self, address):
        """Instance method to send a get to specified address

        returns:
            :output: string output as list of lines
        """
        return self._res.driver.goto_address(address)
