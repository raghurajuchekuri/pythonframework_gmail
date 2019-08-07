from core.runtime import connection_manager
from core.resources.resource import GenericResource

from core.lib.linuxshell import LinuxShell


class Unix(GenericResource):
    """UnixDevice resource class is meant to represent a typical Unix/Linux resource.
    The following attributes are mandatory and must be passed via the testbed YAML file.

    attributes:
        :ip: IP Address of the device
        :user: Username
    """
    def bootstrap(self):
        """This method is used to establish the SSH connection to the device and fill up useful metadata related to
        the device.

        """

        self.shell = connection_manager.get(LinuxShell, self.ip, port=22, user=self.user, password=self.password)

#        distro, version = self._get_distribution()
#        self.os_version = LinuxVersion(distro, version)
        self.connected = True

    def _get_distribution(self):
        """Instance method to get distribution info of a Linux device

        returns:
            Linux distribution and version strings
        """
        output = self.shell.exec_command("cat /etc/*elease")
        return output

