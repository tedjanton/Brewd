from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, DateField
from wtforms.validators import DataRequired


class SipForm(FlaskForm):
    user_id = IntegerField("user_id", validators=[DataRequired()])
    coffee_id = IntegerField("coffee_id", validators=[DataRequired()])
    review = TextAreaField("review")
    rating = IntegerField("rating")
    img_src = StringField("img_src")
    created_at = DateField("created_at")
