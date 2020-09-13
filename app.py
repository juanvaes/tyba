from eve import Eve
from flask import jsonify
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()

from config.config import SETTINGS_FOLDER
from core.auth.auth import TybaAuth

from modules.users.services import blueprint as users_blueprint
from modules.restaurants.services import blueprint as restaurants_blueprint

from modules.users.hooks import hash_password

cors = CORS()

app = Eve(__name__, auth=TybaAuth)

# Initialize extensions
cors.init_app(app)

#blueprints
app.register_blueprint(users_blueprint, url_prefix="/users")
app.register_blueprint(restaurants_blueprint, url_prefix="/restaurants")

# hooks
app.on_insert_users += hash_password

@app.route('/')
def index():
    return jsonify({'app_status': 'running'})

if __name__ == '__main__':
    app.run(debug=True)