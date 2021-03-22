from .db import db


class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    sip_id = db.Column(db.Integer, db.ForeignKey("sips.id"), nullable=False)
    comment = db.Column(db.String(250), nullable=False)

    user = db.relationship("User", back_populates="comments")
    sip = db.relationship("Sip", back_populates="comments")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "shop_id": self.shop_id,
            "comment": self.comment
        }
