'''
typical useage:
client = OpenAMClient(base_url, username, password)
client.authenticate()
'''

import requests
import json
import logging
import http.client

class OpenAMClient:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password
        
        self.id = None
        
        self.increase_logging_level_for_request()
        self.session = requests.Session()
        self.session.trust_env = False

    def print_response(self, response):
        print(f"STATUS = {response.status_code}")
        print("HEADERS:")
        print(response.headers)
        print("JSON DATA:")
        print(response.json())
        print("==========================================")

    def increase_logging_level_for_request(self):
        http.client.HTTPConnection.debuglevel = 1

        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True    

    def authenticate(self):
        url = f"{self.base_url}/authenticate"
        headers = {
            "X-OpenAM-Username": self.username,
            "X-OpenAM-Password": self.password,
            "Accept-API-Version": "resource=2.0, protocol=1.0",
            "Content-Type": "application/json"
        }

        response = self.session.post(url, json = {}, headers = headers)
        self.print_response(response)
        self.id = response.json()["tokenId"]

    #VERY IMPORTANT, DO NOT CALL THIS
    '''
    def create(self):
        url = f"{self.base_url}/users/{self.username}"
        headers = {
            "iplanetDirectoryPro": id,
            "Cache-Control": "no-cache",
            "Accept-API-Version": "resource=1.1, protocol=1.0",
            "Content-Type": "application/json",
            "If-None-Match": "*"
        }
        response = self.session.put(url, json = {"giveName": "Peter"}, headers = headers)
        self.print_response(response)
    '''

    def update(self, attributes):
        url = f"{self.base_url}/users/{self.username}"
        headers = {
            "iplanetDirectoryPro": self.id,
            "Cache-Control": "no-cache",
            "Accept-API-Version": "resource=1.1, protocol=1.0",
            "Content-Type": "application/json",
            "If-None-Match": "_rev"
        }
        response = self.session.put(url, json = attributes, headers = headers)
        self.print_response(response)    

    def read(self):
        #url = f"{self.base_url}/users/{self.username}?_fields=uid"
        url = f"{self.base_url}/users/{self.username}"
        headers = {
            "iplanetDirectoryPro": self.id,
            "Cache-Control": "no-cache",
            "Accept-API-Version": "resource=1.1, protocol=1.0",
            "Content-Type": "application/json"
        }
        response = self.session.get(url, json = {}, headers = headers)
        self.print_response(response)
        return response.json()

    def search(self):
        url = f"{self.base_url}/users?_queryFilter=uid%20eq%20{self.username}"
        headers = {
            "iplanetDirectoryPro": self.id,
            "Cache-Control": "no-cache",
            "Accept-API-Version": "resource=1.1, protocol=1.0",
            "Content-Type": "application/json"
        }
        response = self.session.get(url, json = {}, headers = headers)
        self.print_response(response)

    '''
    at thsi point, this call receives {'code': 400, 'reason': 'Bad Request', 'message': "Unrecognized request parameter '_action'"}
    unclear why yet
    '''
    def is_token_valid(self):
        url = f"{self.base_url}/sessions/tokenId?_action=validate"
        headers = {
            "iplanetDirectoryPro": self.id,
            "Cache-Control": "no-cache",
            "Accept-API-Version": "resource=1.1, protocol=1.0",
            "Content-Type": "application/json"
        }
        response = self.session.get(url, json = {}, headers = headers)
        self.print_response(response)    

    def logout(self):
        url = f"{self.base_url}/sessions/?_action=logout"
        headers = {
            "iplanetDirectoryPro": self.id,
            "Cache-Control": "no-cache",
            "Accept-API-Version": "resource=1.1, protocol=1.0",
            "Content-Type": "application/json"
        }
        response = self.session.post(url, json = {}, headers = headers)
        self.print_response(response)



