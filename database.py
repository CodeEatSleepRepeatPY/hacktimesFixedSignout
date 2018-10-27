import pickle
import utils

users = {}

def add(username, password):
    users[username] = utils.hash(password)

def validate(provided_username, provided_password):
    if provided_username in users:
        if users[provided_username] == utils.hash(provided_password):
            return True
        else:
            return False
    else:
        return False
