import requests

from web import config


def signup(name, email, password):
    payload = {
        "name": name,
        "email": email,
        "password": password,
    }
    headers = {"Content-Type": "application/json"}
    response = requests.request("POST", f"{config.backend_uri}/signup", json=payload, headers=headers)
    return response.json() if response.status_code == 201 else {}


def login(email, password):
    payload = {
        "email": email,
        "password": password,
    }
    headers = {"Content-Type": "application/json"}
    response = requests.request("POST", f"{config.backend_uri}/signin", json=payload, headers=headers)
    token = response.json()["token"] if response.status_code == 200 else ""
    return token


def get_photos(token):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.request("GET", f"{config.backend_uri}/photos", headers=headers)
    photos = response.json()["photos"] if response.status_code == 200 else []
    return photos


def get_photos_pendent(token):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.request("GET", f"{config.backend_uri}/photos/pendent", headers=headers)
    photos = response.json()["photos"] if response.status_code == 200 else []
    return photos
