from eve import Eve
from flask_cors import CORS

from config.config import SETTINGS_FOLDER

cors = CORS()

def create_app(settings_path):
    app = Eve()
    # Initialize extensions
    cors.init_app(app)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()