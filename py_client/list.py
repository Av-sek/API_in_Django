from dataclasses import dataclass
import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"
username = input("What is your username")
password = getpass("What is your pass")

auth_token = requests.post(
    auth_endpoint,
    json={
        "username":username,
        'password':password
    })

if auth_token.status_code==200:
    token = auth_token.json()['token']
    headers = {
        "Authorization":f"Bearer {token}"
    }
    endpoint = "http://localhost:8000/api/products/"
    get_response = requests.get(
        endpoint,
        headers=headers
        )

print(get_response.json())