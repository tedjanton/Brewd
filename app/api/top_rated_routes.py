from app.models import Sip, Coffee, User
from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Sip, Coffee

top_rated_routes = Blueprint('top_rated', __name__)


@top_rated_routes.route('/')
@login_required
def top_rated():
    top_rated = Coffee.query.all()
    # print('HELLO: ', top_rated.sips_rating)
    return {"top_rated": [coffee.to_dict() for coffee in top_rated]}
