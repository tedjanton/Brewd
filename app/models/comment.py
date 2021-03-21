from .db import db


class Comment(db.Model):
    __tablename__ = "likes"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    sip_id = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(250), nullable=False)

    user = db.relationship("User")
    sip = db.relationship("Sip")


    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "shop_id": self.shop_id,
            "comment": self.comment
        }
