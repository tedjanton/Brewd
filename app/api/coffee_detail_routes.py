from app.models import db, Sip, Coffee
from flask_login import login_required
from flask import Blueprint, session, request
from app.forms import SipForm
from datetime import datetime


coffee_detail_routes = Blueprint("coffee_detail_routes", __name__)


@coffee_detail_routes.route("/<int:id>/")
@login_required
def coffee(id):
    coffee = Coffee.query.get(id)

    return {"currentCoffee": coffee.to_dict()}


@coffee_detail_routes.route("/<int:id>/sips/")
@login_required
def coffee_sips(id):
    coffee_sips = Sip.query.filter(Sip.coffee_id == id).all()

    return {"coffeeSips": [sip.to_dict() for sip in coffee_sips]}

@coffee_detail_routes.route("/add-sip/", methods=["POST"])
@login_required
def add_sip():
    """
    Add a Sip to the database
    """
    form = SipForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        new_sip = Sip(user_id=form.user_id.data,
                          coffee_id=form.coffee_id.data,
                          review=form.review.data,
                          rating=form.rating.data,
                          img_src=form.img_src.data,
                          created_at=form.created_at.data)
        db.session.add(new_sip)
        db.session.commit()
        return new_sip.to_dict()
    else:
        return {"errors": "invalid submission"}
