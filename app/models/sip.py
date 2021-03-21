from .db import db


class Sip(db.Model):
    __tablename__ = "sips"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    coffee_id = db.Column(db.Integer, db.ForeignKey(
        "coffees.id"), nullable=False)
    review = db.Column(db.String(250))
    rating = db.Column(db.Integer)
    img_src = db.Column(db.String)
    created_at = db.Column(db.Date)

    user = db.relationship("User")
    coffee = db.relationship("Coffee")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "coffee_id": self.coffee_id,
            "review": self.review,
            "rating": self.rating,
            "img_src": self.img_src,
            "created_at": self.created_at
        }
