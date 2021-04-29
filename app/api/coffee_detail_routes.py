from app.models import db, Sip, Coffee, Image
from flask_login import login_required
from flask import Blueprint, session, request
from app.forms import SipForm
from datetime import datetime
from app.awsS3 import (
    upload_file_to_s3, allowed_file, get_unique_filename)


coffee_detail_routes = Blueprint("coffee_detail_routes", __name__)


@coffee_detail_routes.route("/<int:id>/")
@login_required
def coffee(id):
    coffee = Coffee.query.get(id)

    return {"currentCoffee": coffee.to_dict()}


@coffee_detail_routes.route("/<int:id>/sips/")
@login_required
def coffee_sips(id):
    coffee_sips = Sip.query.filter(Sip.coffee_id == id).order_by(Sip.created_at.desc()).all()

    return {"coffeeSips": [sip.to_dict() for sip in coffee_sips]}


@coffee_detail_routes.route("/image/", methods=["POST"])
@login_required
def upload_image():

    if "image" not in request.files:
        return {"errors": "image required"}, 400
    image = request.files["image"]
    if not allowed_file(image.filename):
        return {"errors": "file type not permitted"}, 400
    image.filename = get_unique_filename(image.filename)
    print(image)
    upload = upload_file_to_s3(image)
    print(upload)
    if "url" not in upload:
        return upload, 400
    url = upload["url"]

    coffee_image = Image(url=url)

    db.session.add(coffee_image)
    db.session.commit()
    return {"url": url}


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
