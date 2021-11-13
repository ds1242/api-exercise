from flask import Blueprint, request, jsonify, session, redirect
from pprint import pprint
from app.models import Data
from app.db import get_db
import json

bp = Blueprint('batch_jobs', __name__, url_prefix='/batch_jobs')

# @bp.route('/')
# def index():
#     db = get_db()
#     data = db.query(Data).all()
#     return jsonify(data)





@bp.route('/')
def index():
    db = get_db()
    one_row = db.query(Data).first()
    # data_schema = DataSchema()
    # output = json.dumps(one_row).data
    # return jsonify({'batch_jobs': output})
    pprint(vars(one_row))
    return jsonify({'batch_jobs': '1'})
