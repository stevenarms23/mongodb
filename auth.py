import bcrypt
from db import users


def register(username: str, password: str):
    if users.find_one({"username": username}):
        return "User already exists"

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    users.insert_one({
        "username": username,
        "password": hashed
    })
    return "User registered"


def login(username: str, password: str):
    user = users.find_one({"username": username})
    if not user:
        return "Invalid credentials"

    if bcrypt.checkpw(password.encode(), user["password"]):
        return "Login successful"
    return "Invalid credentials"
