## login.py

import json

DIRECTORY_FILE = "assets/data/users.json"

def load_directory():
    with open(DIRECTORY_FILE, "r") as file:
        return json.load(file)

def save_directory(data):
    with open(DIRECTORY_FILE, "w") as file:
        json.dump(data, file, indent = 4)

def save_user(updated_user):
    data = load_directory()
    for i, user in enumerate(data["users"]):
        if user["username"] == updated_user["username"]:
            data["users"][i] = updated_user
            break

    save_directory(data)
def check_credentials(username, password):

    data = load_directory()
    for user in data["users"]:
        if (user["username"] == username and user["password"] == password):
            return user
    return None
def spend_token(username):
    data = load_directory()
    for user in data["users"]:
        if user["username"] == username:
            if user["tokens"] <= 0:
                return False
            user["tokens"] -= 1
            save_directory(data)
            return True
        
    return False

def get_tokens(username):
    data = load_directory()

    for user in data["users"]:
        if user["username"] == username:
            return user["tokens"]

    return 0

