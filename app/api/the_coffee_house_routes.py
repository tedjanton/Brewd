from flask import Blueprint, jsonify, request, session
from flask_login import login_required
from app.models import db, Sip, Coffee, User

the_coffee_house_routes = Blueprint('coffeehouse', __name__)


@the_coffee_house_routes.route('/')
@login_required
def recent_sips():
    all_sips = Sip.query.order_by(Sip.created_at.desc()).all()

    return {"all_sips": [sip.to_dict() for sip in all_sips]}


@the_coffee_house_routes.route("/edit-sip/<int:id>/", methods=["POST"])
@login_required
def edit_sip(id):
    req = request.get_json()
    sip = Sip.query.get(id)
    sip.review = req["review"]
    sip.rating = req["rating"]
    sip.img_src = req["img_src"]
    db.session.commit()
    return sip.to_dict()


@the_coffee_house_routes.route("/<int:id>/delete/", methods=["GET"])
@login_required
def delete_sip(id):
    sip = Sip.query.get(id)
    db.session.delete(sip)
    db.session.commit()
    return sip.to_dict()
