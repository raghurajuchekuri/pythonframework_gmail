from time import strftime
import hmac
import requests
import time
import hashlib

import json

import core


class ApiBuilder:

    @staticmethod
    def set_auth_header(merchant_code, header_type):

        account_id = 1234
        db_actor = core.get(core.res['mysql'], feature="dbaccess")
        key = db_actor.get_account_details(account_id, key_name="IpnKey").encode()

        date = strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        string = (str(len(merchant_code))+merchant_code+str(len(date))+date).encode()
        hash_key = hmac.new(key, string, hashlib.md5)
        if header_type is "API":
            header = {
                "Content-Type": "application/json",
                "Accept": "application/json",
            }

            return header
        else:
            raise Exception("Please select header. The two options are 'API'.")

    def api_call(self, host_url, header_type, http_method, request_data=None, code=None):

        timeout = 30

        """Method to create -Authentication headers.

            args:
                :host_url (str): API url endpoint.
                :header_type (str): The API version to be used for testing. API(Default)|.
                :http_method (str): The http method that it is used for the request (POST, GET, PUT, DELETE)
                :request_data (dict): Dictionary where user can specify the entire body of the request.
                :code (int): Vendor ID account.

            returns:
                An array contains Authentication headers value.
        """
        supported_http_methods = ["POST", "GET", "PUT", "DELETE"]
        if http_method not in supported_http_methods:
            raise ValueError(f"'{http_method}' method is not supported: Current supported methods: "
                             f"{supported_http_methods}")
        header = ApiBuilder.set_auth_header(code, header_type)

        if http_method is "POST":
            response = requests.post(host_url, data=json.dumps(request_data), headers=header)
        elif http_method is "GET":
            response = requests.get(host_url, headers=header, timeout=timeout)
        elif http_method is "PUT":
            response = requests.put(host_url, data=json.dumps(request_data), headers=header)
        elif http_method is "DELETE":
            response = requests.delete(host_url, data=json.dumps(request_data), headers=header)

        if (response.content and response.status_code) is None:
            raise Exception(f"Request to: {host_url}, action: {http_method} failed with error: {response.status_code}")
        else:
            return response

