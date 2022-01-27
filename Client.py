import requests
import json

class Client:
    def __init__(self, base_url):
        self.base_url = base_url

    def register(self, name, email, password):
        url = self.base_url + "/register"
        payload = json.dumps({
            "name": name,
            "email": email,
            "password": password
        })
        headers = {
            'Content-Type': 'application/json'
        }
        return requests.request("POST", url, headers=headers, data=payload)

    def login_check(self, username, password):
        url = self.base_url + "/api/login_check"
        payload = json.dumps({
            "username": username,
            "password": password
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response     = requests.request("POST", url, headers=headers, data=payload)
        responseJson = json.loads(response.text)
        self.token   = responseJson['token']
        return response

    def create_task(self, text):
        url = self.base_url + "/api/task"
        payload = json.dumps({
            "text": text
        })
        headers = {
            'Authorization': 'Bearer ' + self.token,
            'Content-Type': 'application/json'
        }
        return requests.request("POST", url, headers=headers, data=payload)

    def get_all_tasks(self):
        url = self.base_url + "/api/task"
        headers = {
            'Authorization': 'Bearer ' + self.token,
            'Content-Type': 'application/json'
        }
        return requests.request("GET", url, headers=headers)

    def get_task(self, num):
        url = self.base_url + "/api/task/" + str(num)
        headers = {
            'Authorization': 'Bearer ' + self.token,
            'Content-Type': 'application/json'
        }
        return requests.request("GET", url, headers=headers)

    def delete_task(self, num):
        url = self.base_url + "/api/task/" + str(num)
        headers = {
            'Authorization': 'Bearer ' + self.token,
            'Content-Type': 'application/json'
        }
        return requests.request("DELETE", url, headers=headers)

    def edit_task(self, text, num):
        url = self.base_url + "/api/task/" + str(num)
        payload = json.dumps({
            "text": text
        })
        headers = {
            'Authorization': 'Bearer ' + self.token,
            'Content-Type': 'application/json'
        }
        return requests.request("PUT", url, headers=headers, data=payload)