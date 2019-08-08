import configparser
import os

import peewee

DATABASES = ['databases.conf']
SUPPORTED_DB_TYPES = ['mysql']


class DbConnection:
    DB = None

    def __init__(self, host, user, password, db_name='automation', db_type='mysql', port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name
        self.port = port
        self.cursor = None
        self.db_connection = None
        # if db_type == "mysql":
        #     # self.db_connection = self.connect_mysql_db()
        #     # self.cursor = self.db_connection.cursor()
        #
        # elif db_type not in SUPPORTED_DB_TYPES:
        #     raise ValueError(f"{db_type} is currently not supported; Supported DB types: {SUPPORTED_DB_TYPES}")

    def connect_mysql_db(self):
        """ Establishing database connection.

            returns
                Connection to database.
        """
        mysql = peewee.mysql.connect(host=self.host,
                                     user=self.user,
                                     password=self.password,
                                     port=self.port,
                                     db=self.db_name,
                                     charset='utf8', )
        return mysql


def config_parser():
    """Utility function to return an instance of the ConfigParser class.

    returns:
        An instance of the ConfigParser class.
    """
    conf = configparser.ConfigParser()
    conf.optionxform = str

    return conf


def database_info():
    """Function to load the database conf file.

    returns:
        Parsed ini config.

    """
    conf = config_parser()
    conf.read(os.path.join(os.path.dirname(__file__), DATABASES))

    return conf
