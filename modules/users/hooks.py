from passlib.handlers.pbkdf2 import pbkdf2_sha512


def hash_password(items, lookup=None):
    for item in items:
        password = item['password']
        item['password'] = pbkdf2_sha512.hash(password)