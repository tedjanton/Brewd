from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import db, Sip, Coffee

top_rated_routes = Blueprint('top_rated', __name__)


@top_rated_routes.route('/')
# @login_required
def top_rated():
    # top_rated = Sip.query.order_by(Sip.rating).all()
    # individual = top_rated[0].to_dict()
    top_rated = Coffee.query.join(Sip).filter(Sip.rating == 4)
    print('HELLO: ', top_rated.name)
    # return {"top_rated": [top_rated.to_dict() for coffee in top_rated]}
    return "hi"
