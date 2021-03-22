from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import db, Sip

top_rated_routes = Blueprint('top_rated', __name__)


@top_rated_routes.route('/')
# @login_required
def top_rated():
    top_rated = Sip.query.order_by(Sip.rating)
    print('HELLO: ', top_rated)
    return {"top_rated": [top_rated.to_dict() for sip in top_rated]}
