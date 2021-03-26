from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Coffee, Shop

coffeeshop_details_routes = Blueprint('shop', __name__)

@coffeeshop_details_routes.route("/<int:id>/")
@login_required
def shop_and_coffees(id):
    shop = Shop.query.get(id)
    coffees = Coffee.query.filter(Coffee.shop_id == id).all()
    return {"individual_shop": shop.to_dict(),
            "coffees_by_shop": [coffee.to_dict() for coffee in coffees]}
