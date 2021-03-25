from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired


class LikeForm(FlaskForm):
    user_id = IntegerField("user_id", validators=[DataRequired()])
    sip_id = IntegerField("sip_id", validators=[DataRequired()])
