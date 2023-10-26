import os

def authenticated(key: str):
    secret = os.getenv('SECRET_KEY')
    return key == secret