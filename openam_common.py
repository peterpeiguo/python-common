import requests
import json
import logging
import http.client

def print_response(response):
    print(f"STATUS = {response.status_code}")
    print("HEADERS:")
    print(response.headers)
    print("JSON DATA:")
    print(response.json())
    print("==========================================")

def increase_logging_level_for_request():
    http.client.HTTPConnection.debuglevel = 1

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True    

def get_seesion():
    session = requests.Session()
    session.trust_env = False
    return session

def authenticate(session, base_url, username, password):
    url = f"{base_url}/authenticate"
    headers = {
        "X-OpenAM-Username": username,
        "X-OpenAM-Password": password,
        "Accept-API-Version": "resource=2.0, protocol=1.0",
        "Content-Type": "application/json"
    }

    response = session.post(url, data = {}, headers = headers)
    print_response(response)
    return response.json()["tokenId"]

def attributes(session, base_url, id, username):
    url = f"{base_url}/users/{username}"
    headers = {
        "iplanetDirectoryPro": id,
        "Cache-Control": "no-cache",
        "Accept-API-Version": "resource=1.1, protocol=1.0",
        "Content-Type": "application/json"
    }
    response = session.get(url, data = {}, headers = headers)
    print_response(response)
    return response.json()

#VERY IMPORTANT, DO NOT CALL THIS
def create(session, base_url, id, username):
    url = f"{base_url}/users/{username}"
    headers = {
        "iplanetDirectoryPro": id,
        "Cache-Control": "no-cache",
        "Accept-API-Version": "resource=1.1, protocol=1.0",
        "Content-Type": "application/json",
        "If-None-Match": "*"
    }
    response = session.put(url, json = {"giveName": "Peter"}, headers = headers)
    print_response(response)

def update(session, base_url, id, username, attributes):
    url = f"{base_url}/users/{username}"
    headers = {
        "iplanetDirectoryPro": id,
        "Cache-Control": "no-cache",
        "Accept-API-Version": "resource=1.1, protocol=1.0",
        "Content-Type": "application/json",
        "If-None-Match": "_rev"
    }
    response = session.put(url, json = attributes, headers = headers)
    print_response(response)    

def read(session, base_url, id, username):
    #url = f"{base_url}/users/{username}?_fields=uid"
    url = f"{base_url}/users/{username}"
    headers = {
        "iplanetDirectoryPro": id,
        "Cache-Control": "no-cache",
        "Accept-API-Version": "resource=1.1, protocol=1.0",
        "Content-Type": "application/json"
    }
    response = session.get(url, data = {}, headers = headers)
    print_response(response)

def search(session, base_url, id, username):
    url = f"{base_url}/users?_queryFilter=uid%20eq%20{username}"
    headers = {
        "iplanetDirectoryPro": id,
        "Cache-Control": "no-cache",
        "Accept-API-Version": "resource=1.1, protocol=1.0",
        "Content-Type": "application/json"
    }
    response = session.get(url, data = {}, headers = headers)
    print_response(response)

def is_token_valid(session, base_url, id):
    url = f"{base_url}/sessions/tokenId?+action=validate"
    headers = {
        "iplanetDirectoryPro": id,
        "Cache-Control": "no-cache",
        "Accept-API-Version": "resource=1.1, protocol=1.0",
        "Content-Type": "application/json"
    }
    response = session.get(url, data = {}, headers = headers)
    print_response(response)    

def logout(session, base_url, id):
    url = f"{base_url}/sessions/?_action=logout"
    headers = {
        "iplanetDirectoryPro": id,
        "Cache-Control": "no-cache",
        "Accept-API-Version": "resource=1.1, protocol=1.0",
        "Content-Type": "application/json"
    }
    response = session.post(url, data = {}, headers = headers)
    print_response(response)



