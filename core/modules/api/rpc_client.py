import json
import requests

from core.modules.api import APIClient


class RpcClient(APIClient):
    """This class represents a client that routes all RPC calls, it extends the generic APIClient in order to inherit
    methods needed for setup and login.
    The class variable ID is needed for all RPC calls and is used to track subsequent calls.
    """
    ID = 1

    def __init__(self):
        super().__init__()
        self.headers = self.get_headers()

    def rpc_login(self, host_url):
        """Method that uses the secret key encoded hash in order to generate the session id needed for login.

        args:
            host_url (str): API url endpoint.

        returns:
            The session id (str) that is used for any RPC module_api call.
        """
        json_rpc_request = {
            'jsonrpc': '2.0',
            'method': 'login',
            'params': [self.merchant_code, self.get_date(), self.get_hash().hexdigest()],
            'id': self.ID
        }

        self.ID += 1
        session_id_dict = requests.post(host_url, data=json.dumps(json_rpc_request), headers=self.headers)
        session_id = session_id_dict.text.replace("'", "\"")
        session_id = json.loads(session_id)

        return session_id['result']

    def api_call(self, method, host, params):
        """Method used to perform RPC module_api calls, it uses the rpc_login(host) method in order to generate the
        session id, which is always the first parameter of a RPC method.

        args:
            method (str): The name of the method you want to perform the call for.
            host (str): API url endpoint.
            params (str): The parameters that are needed for the RPC method.
            TODO: Refactor params as a dict and grab values from it.

        returns:
            The response dictionary that the server returns.
        """
        session_id = self.rpc_login(host)

        json_rpc_request = {
            'jsonrpc': '2.0',
            'method': method,
            'params': [session_id, params],
            'id': self.ID
        }

        self.ID += 1
        response = requests.post(host, data=json.dumps(json_rpc_request), headers=self.headers)

        return response
