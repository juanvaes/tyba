import requests
from flask import Blueprint, current_app as app, request, jsonify

from domains import USERS_DOMAIN

from core.auth.decorators import login_required
from modules.restaurants.utils import ZOMATO_API_KEY, ZOMATO_API_URI, ZOMATO_API_HEADERS


blueprint = Blueprint('restaurants', __name__)

@blueprint.route('', methods=['GET'])
@login_required
def get_restaurants():
    city = request.args.get('city')
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    if city:
        location_response = requests.get(
            url = ZOMATO_API_URI + '/locations',
            params={'query': city},
            headers=ZOMATO_API_HEADERS
        )
        if location_response.status_code in (200, 201):
            json_data = location_response.json()
            locations = json_data.get('location_suggestions')
            if len(locations) > 0:
                location = locations[0]
                lat, lon = location.get('latitude'), location.get('longitude')
            elif len(locations) == 0:
                return jsonify({'response': 'no restaurants were found for this city'})

    restaurants_response = requests.get(
        url = ZOMATO_API_URI + '/search',
        params={'lat': lat, 'lon': lon},
        headers=ZOMATO_API_HEADERS
    )
    if restaurants_response.status_code in (200, 201):
        json_response = restaurants_response.json()
        restaurants_list = json_response.get('restaurants', [])
        if len(restaurants_list) > 0:
            return jsonify({'response': restaurants_list})
        else:
            jsonify({'response': 'no restaurants were found for this city'})
    else:
        return jsonify({'response': 'no restaurants were found for this city'})
