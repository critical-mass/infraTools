import json
import requests


class okta:
    def __init__(self, user_id, base_url, headers, group_id):
        self.user_id = user_id
        self.base_url = base_url
        self.headers = headers
        self.group_id = group_id
        self.description = description
        self.create_group = group_name


    def read_user(user_id, base_url, headers):
        url = f"{base_url}/api/v1/users/{user_id}"
        payload = {}
        response = requests.get(url, headers=headers, data=payload)
        return(response)

    def activate_user(user_id, base_url, headers):
        url = f"{base_url}/api/v1/users/{user_id}/lifecycle/activate?sendEmail=true"
        payload = {}
        response = requests.post(url, headers=headers, data=payload)
        return(response)

    def deactivate_user(user_id, base_url, headers):
        url = f"{base_url}/api/v1/users/{user_id}/lifecycle/deactivate"
        payload = {}
        response = requests.post(url, headers=headers, data=payload)
        return(response)

    def add_user_to_group(user_id, base_url, headers, group_id):
        url = f"{base_url}/api/v1/groups/{group_id}/users/{user_id}"
        payload = {}
        response = requests.post(url, headers=headers, data=payload)
        return(response)

    def create_group(base_url, group_name, description, headers):
        url = f"{base_url}/api/v1/groups/"
        payload = {
            "profile": {
                "description": description,
                "name": group_name
            }
        }
        response = requests.post(url, headers=headers, data=payload)
        return(response)

   def create_user(base_url, firstName, lastName, email, login, headers):
       url = f"{base_url}/api/v1/users
       payload = {
           "profile": {
               "firstName": firstName,
               "lastName": lastName,
               "email": email,
               "login": login,
           }
       }
       response = requests.post(url=url, headers=headers, data=payload)
