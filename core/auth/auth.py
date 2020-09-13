import os
import jwt
import logging

from eve.auth import TokenAuth
from flask import current_app as app
from bson import ObjectId

from domains import USERS_DOMAIN

AVOID_AUTH_RESOURCE_LIST = [USERS_DOMAIN]

class TybaAuth(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
        user = None
        db = app.data.driver.db
        token_data = jwt.decode(token, app.config.get('SECRET_KEY'), algorithm='HS256')
        if 'user_id' in token_data:
            user_id = token_data.get('user_id')
            user = db[USERS_DOMAIN].find_one({'_id': ObjectId(user_id)})
            if not user:
                return False
            self.set_user_or_token(user_id)
            return True 
        return False


def generate_token(**kwargs):
    return {'token': jwt.encode(kwargs, app.config.get('SECRET_KEY'), algorithm='HS256')}