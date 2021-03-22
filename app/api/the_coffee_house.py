from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Sip

the_coffee_house_routes = Blueprint('coffeehouse', __name__)


@the_coffee_house_routes.route('/')
@login_required
def recent_sips():
    sips = Sip.query.order_by(Sip.created_at).all()
    return {"sips": [sip.to_dict() for sip in sips]}
