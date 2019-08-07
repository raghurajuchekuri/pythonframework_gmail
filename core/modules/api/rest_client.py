import requests
import json

from core.modules.api import APIClient


class RestClient(APIClient):
    """This class represents a client that routes all REST calls, it extends the generic APIClient in order to inherit
    methods needed for setup and login.
    """
    def __init__(self):
        super().__init__()
        self.hash = self.get_hash()

    @staticmethod
    def rest_login_headers(self):
        """A method used to generate AUTH headers in order to make the rest calls."""
        self.header = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            'X-Avangate-Authentication': f'code="{self.merchant_code}" date="{self.get_date()}" '
                                         f'hash="{self.hash.hexdigest()}"',
        }

        return self.header

    def api_call(self, host_url, http_method, request_data=None):

        timeout = 30

        """Method to create headers.

            args:
                :host_url (str): API url endpoint.
                :http_method (str): The http method that it is used for the request (POST, GET, PUT, DELETE)
                :request_data (dict): Dictionary where user can specify the entire body of the request.
            returns:
                An array
        """
        supported_http_methods = ["POST", "GET", "PUT", "DELETE"]
        if http_method not in supported_http_methods:
            raise ValueError(f"'{http_method}' method is not supported: Current supported methods: "
                             f"{supported_http_methods}")
        header = RestClient.rest_login_headers(self)

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

