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
            avg_rating = round(sum(ratings)/len(ratings), 1)

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
        return {
            "id": self.id,
            "shop_id": self.shop_id,
            "name": self.name,
            "description": self.description,
            "caffeine": self.caffeine,
            "type": self.type,
            "img_src": self.img_src,
            "shop": self.shop.to_dict(),
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
