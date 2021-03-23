from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import db, Sip, Coffee

top_rated_routes = Blueprint('top_rated', __name__)


@top_rated_routes.route('/')
@login_required
def top_rated():
    top_rated = Sip.query.order_by(Sip.rating).all()
    for sip in top_rated:
        top_coffee = sip.coffee
    print('HELLO: ', top_coffee)
    # return "hi"
    return top_coffee.to_dict()

