from eve.methods.post import post_internal
from flask import Blueprint, current_app as app, request, jsonify
from passlib.handlers.pbkdf2 import pbkdf2_sha512

from domains import USERS_DOMAIN
from core.auth.auth import generate_token


blueprint = Blueprint('users', __name__)


@blueprint.route('/login', methods=['POST'])
def make_login():
    data = request.json
    if not 'email' in data or not 'password' in data:
        return jsonify({'response': 'invalid input'})
    db = app.data.driver.db
    user = db[USERS_DOMAIN].find_one({
        'email': data.get('email')
    })
    if not user:
        return jsonify({'response': 'invalid username or password'})
    
    if pbkdf2_sha512.verify(data['password'], user.get('password')):
        return jsonify(generate_token(user_id=str(user.get('_id'))))


@blueprint.route('/register', methods=['POST'])
def make_register():
    data = request.json
    if not 'email' in data or not 'password' in data:
        return jsonify({'response': 'invalid input'})
    db = app.data.driver.db
    if db[USERS_DOMAIN].find_one({"email": data['email']}):
        return jsonify({"response": "user registered"})

    response = post_internal(
        USERS_DOMAIN,
        {
            'first_name': data.get('first_name', ''),
            'last_name': data.get('last_name', ''),
            'email': data.get('email'),
            'password': data.get('password')
        })
    response = response[0]
    return jsonify({"response": "user registered"})
