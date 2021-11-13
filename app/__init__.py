from flask import Flask
from app.models import Data
from app.db import init_db
from app.routes import api
# from flask_marshmallow import Marshmallow



def create_app(test_config=None):
    # set up config
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes=False
    app.config.from_mapping(
        SECRET_KEY='super_secret_key'
    )

    app.register_blueprint(api)

    init_db(app)

    # ma = Marshmallow(app)
    # class DataSchema(ma.ModelSchema):
    #     class Meta:
    #         model = Data


    return app
