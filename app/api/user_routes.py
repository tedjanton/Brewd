from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Sip


user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    users = User.query.all()
    return {"users": [user.to_dict() for user in users]}


@user_routes.route('/<int:id>/')
@login_required
def user(id):
    user = User.query.get(id)
    return user.to_dict()


@user_routes.route('/<int:id>/sips/')
@login_required
def user_sips(id):
    user_sips = Sip.query.filter(Sip.user_id == id).order_by(Sip.created_at.desc()).all()
    return {"user_sips": [sips.to_dict() for sips in user_sips]}
