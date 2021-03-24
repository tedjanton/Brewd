from app.models import db, Sip, Coffee
from flask_login import login_required
from flask import Blueprint
from app.forms import SipForm

coffee_detail_routes = Blueprint("coffee_detail_routes", __name__)


@coffee_detail_routes.route("/<int:id>")
@login_required
def coffee(id):
    coffee = Coffee.query.get(id)
    return coffee.to_dict()


@coffee_detail_routes.route("/add-sip", methods=["POST"])
@login_required
def add_sip():
    """
    Adds a Sip to the database
    """
    form = SipForm()
    if form.validate_on_submit():
        new_sip = SipForm(user_id=form.user_id.data,
                          coffee_id=form.coffee_id.data,
                          review=form.review.data,
                          rating=form.rating.data,
                          img_src=form.img_src.data,
                          created_at=form.created_at.data)
        db.session.add(new_sip)
        db.session.commit()
        print("SUCCESSSSSSSSSS")
        return new_sip.to_dict()
    else:
        return {"errors": "invalid submission"}
