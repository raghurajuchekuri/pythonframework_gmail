from core.runtime import connection_manager
from core.resources.resource import GenericResource

from core.lib.database import DbConnection


class Database(GenericResource):
    """Database resource class is meant to represent a typical MySql resource.
    The following attributes are mandatory and must be passed via the testbed YAML file.

    attributes:
        :host: Host Address of the database.
        :port: Port of the database.
        :user: Username of the database used for connection
        :password: Password of the database used for connection.
    """
    def bootstrap(self):
        """This method is used to establish the connection to the device and fill up useful metadata related to
        the device.

        """

        self.db = connection_manager.get(DbConnection, host=self.ip, port=3306, user=self.user, password=self.password)

        self.connected = True

