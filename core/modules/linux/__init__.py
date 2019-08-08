from core.modules import GenericFeature


class Linux(GenericFeature):
    """Shell defines the interface to execute actions on a host running linux OS.
    """
    def get_distribution(self):
        """Instance method to get lsb_release_info on a linux based device.

        returns:
            :output: string output as list of lines
        """
        pass

    def exec_command(self, command):
        pass
