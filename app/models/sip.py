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

    user = db.relationship("User", back_populates="sips")
    coffee = db.relationship("Coffee", back_populates="sips")
    comments = db.relationship("Comment", back_populates="sip")
    likes = db.relationship("Like", back_populates="sip")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "coffee_id": self.coffee_id,
            "review": self.review,
            "rating": self.rating,
            "img_src": self.img_src,
            "created_at": self.created_at,
            "user": self.user.to_dict(),
            "coffee": self.coffee.to_dict(),
            # "comments": self.comments.to_dict(),
            # "likes": self.likes.to_dict()
        }
