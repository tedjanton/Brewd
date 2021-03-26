from .db import db


class Coffee(db.Model):
    __tablename__ = "coffees"

    id = db.Column(db.Integer, primary_key=True)
    shop_id = db.Column(db.Integer, db.ForeignKey("shops.id"), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String)
    caffeine = db.Column(db.Integer)
    type = db.Column(db.String(4), nullable=False)
    img_src = db.Column(db.String)

    shop = db.relationship("Shop", back_populates="coffees")
    sips = db.relationship("Sip", back_populates="coffee")

    def to_dict(self):
        ratings = []

        for sip in self.sips:
            ratings.append(sip.get_rating())

        if len(ratings) == 1:
            avg_rating = ratings[0]
        elif len(ratings) == 0:
            avg_rating = 0;
        else:
            avg_rating = sum(ratings)/len(ratings)

        return {
            "id": self.id,
            "shop_id": self.shop_id,
            "name": self.name,
            "description": self.description,
            "caffeine": self.caffeine,
            "type": self.type,
            "img_src": self.img_src,
            "shop": self.shop.to_dict(),
            "sips": [sip.to_simple_dict() for sip in self.sips],
            "avg_rating": avg_rating,
            "all_ratings": ratings
        }

    def to_simple_dict(self):

        # ratings = []

        # for sip in self.sips:
        #     ratings.append(sip.get_rating())

        # if len(ratings) == 1:
        #     avg_rating = ratings[0]
        # elif len(ratings) == 0:
        #     avg_rating = 0;
        # else:
        #     avg_rating = sum(ratings)/len(ratings)
            
        return {
            "id": self.id,
            "shop_id": self.shop_id,
            "name": self.name,
            "description": self.description,
            "caffeine": self.caffeine,
            "type": self.type,
            "img_src": self.img_src,
            "shop": self.shop.to_dict(),
            # "avg_rating": avg_rating,
            # "all_ratings": ratings
        } 

        
    def to_shop_dict(self):

        ratings = []

        for sip in self.sips:
            ratings.append(sip.get_rating())

        if len(ratings) == 1:
            avg_rating = ratings[0]
        elif len(ratings) == 0:
            avg_rating = 0;
        else:
            avg_rating = sum(ratings)/len(ratings)
            
        return {
            "id": self.id,
            # "shop_id": self.shop_id,
            "name": self.name,
            "description": self.description,
            "caffeine": self.caffeine,
            "type": self.type,
            "img_src": self.img_src,
            "avg_rating": avg_rating,
            "all_ratings": ratings
        } 


# {'id': 1,
# 'user_id': 1,
# 'coffee_id': 1,
# 'review': 'Super tasty! Would highly recommend to anyone.',
# 'rating': 5,
# 'img_src': '',
# 'created_at': datetime.date(2020, 8, 24),
# 'user': {'id': 1,
#         'username': 'Demo',
#         'first_name': 'Demo',
#         'last_name': 'Lition',
#         'email': 'demo@lition.com'},
#         'coffee': {'id': 1,
#                     'shop_id': 1,
#                     'name': 'Golden Mylk Latte',
#                     'description': 'An ancient Indian Elixir. Almond Milk, Honey, Turmeric, Cinnamon, Ginger, Ashwagandha, Black Pepper, Espresso (Double Shot)',
#                     'caffeine': 203,
#                     'type': 'hot',
#                     'img_src': 'https://brewd.s3.amazonaws.com/coffee-pics/01-golden-mylk-latte.jpeg',
#                     'shop': {'id': 1, 'name': 'Oromo Cafe', 'description': "This is a veritable United Nations for coffee, as Oromo Cafe takes flavors from Africa, India and Turkey to offer some of Chicago's most-unique coffee drinks. Oromo also spikes its beverages with superfoods for added nutrients in the drinks.", 'address_1': '4703 N Lincoln Ave', 'address_2': '', 'city': 'Chicago', 'state': 'Illinois', 'zip_code': 60625, 'logo_src': 'https://brewd.s3.amazonaws.com/shop-logos/oromo_cafe_logo.jpeg'}}, 'comments': [], 'likes': []}
