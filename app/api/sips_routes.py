from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Sip, Coffee, User

sips_routes = Blueprint('sips', __name__)


@sips_routes.route('/')
@login_required
def recent_sips():
    all_sips = Sip.query.order_by(Sip.created_at).all()

    return {"all_sips": [sip.to_dict() for sip in all_sips]}
