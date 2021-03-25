from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Sip, Coffee, User

the_coffee_house_routes = Blueprint('coffeehouse', __name__)


@the_coffee_house_routes.route('/')
@login_required
def recent_sips():
    all_sips = Sip.query.order_by(Sip.created_at.desc()).all()
    print("ALL_SIPS", all_sips)

    return {"all_sips": [sip.to_dict() for sip in all_sips]}
