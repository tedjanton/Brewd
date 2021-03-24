from app.models import Sip, Coffee, User
from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Sip, Coffee
from sqlalchemy import func

top_rated_routes = Blueprint('top_rated', __name__)


@top_rated_routes.route('/')
@login_required
def top_rated():
    # highest_rated = Sip.query.filter(Sip.rating > 3)
    top_rated = Coffee.query.all()
    print('HELLO: ', top_rated)
    return {"top_rated": [coffee.to_dict() for coffee in top_rated]}
