"""This sample contains the base APIClient template, which has all the methods needed to create the hash for the login.
All other clients extend this class and use it to generate the session id.
"""
import hmac
import time
import hashlib
import core

from time import strftime


class APIClient:
    """ Blueprint for an module_api client, all module_api clients should extend this class. """

    def __init__(self, account_id=1234):
        """Init method for APIClient

        kwargs:
            :account_id (int): The vendor's account id used for module_api calls
        """
        self.account_id = account_id
        self.db_actor = core.get(core.res['mysql'], feature="db")
        self.secret_key = self.db_actor.get_account_details(self.account_id, key_name="IpnKey").encode()
        self.merchant_code = self.db_actor.get_account_details(self.account_id, key_name="ClientCode")
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    @staticmethod
    def get_date():
        """Method to get the current date in Y-M-D H:M:S format

        returns:
            A current date string
        """
        return strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

    def get_headers(self):
        """Method to get the standard headers used for module_api calls.

        returns:
            A dict containing the standard headers
        """
        return self.headers

    def get_hash(self):
        """Method that uses the merchant_code and the secret key in order to generate the hash needed for login.

        returns:
            An md5 encrypted hash
        """
        string = (str(len(self.merchant_code)) + self.merchant_code + str(
            len(self.get_date())) + self.get_date()).encode()
        return hmac.new(self.secret_key, string, hashlib.md5)
