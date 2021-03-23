from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Sip, Coffee, User

featured_routes = Blueprint('featured', __name__)


@featured_routes.route('/')
@login_required
def recent_sips():
    featured_coffees = Coffee.query.limit(10).all()

    return {"featured_coffees": [coffees.to_dict() for coffees in featured_coffees]}