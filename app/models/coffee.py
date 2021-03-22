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

    shop = db.relationship("Shop", back_populates="coffee")


    def to_dict(self):
        return {
            "id": self.id,
            "shop_id": self.shop_id,
            "name": self.name,
            "description": self.description,
            "caffeine": self.caffeine,
            "type": self.type,
            "img_src": self.img_src
        }
