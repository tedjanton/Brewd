from .db import db


class Like(db.Model):
    __tablename__ = "likes"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    sip_id = db.Column(db.Integer, db.ForeignKey("sips.id"), nullable=False)

    user = db.relationship("User", back_populates="likes")
    sip = db.relationship("Sip", back_populates="likes")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "shop_id": self.shop_id
        }
