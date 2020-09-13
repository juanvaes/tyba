import jwt
from bson import ObjectId

from functools import wraps
from flask import current_app as app, jsonify, request

from domains import USERS_DOMAIN

def login_required(func):
    @wraps(func)
    def wrapper_login_required(*args, **kwargs):
        token = request.headers.get('Authorization')
        token = jwt.decode(token, app.config.get('SECRET_KEY'), algorithm='HS256')
        user_id = token.get('user_id')
        if not user_id:
            return jsonify({'response': 'invalid credentials'})
        db = app.data.driver.db
        user = db[USERS_DOMAIN].find_one({"_id": ObjectId(user_id)})
        if not user:
            return jsonify({'response': 'invalid credentials'})
        return func(*args, **kwargs)
    return wrapper_login_required