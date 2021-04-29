from .db import db


class Image(db.Model):
    __tablename__ = "images"

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "url": self.url,
        }
