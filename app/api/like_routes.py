from app.models import db, Like
from flask_login import login_required
from flask import Blueprint, session, request
from app.forms import LikeForm

like_routes = Blueprint('like_routes', __name__)


@like_routes.route('/', methods=["POST"])
@login_required
def add_like():
    form = LikeForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        new_like = Like(user_id=form.user_id.data, sip_id=form.sip_id.data)
        db.session.add(new_like)
        db.session.commit()
        return new_like.to_dict()
    else:
        return {"errors": "invalid like submission"}

@like_routes.route("/<int:id>/", methods=["GET"])
@login_required
def delete_like(id):
    like = Like.query.filter_by(id).delete()

    db.session.delete(like)
    db.session.commit()
    return {"Success"}
