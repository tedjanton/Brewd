from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField
from wtforms.validators import DataRequired
# from datetime import datetime


class CommentForm(FlaskForm):
    user_id = IntegerField("user_id", validators=[DataRequired()])
    sip_id = IntegerField("sip_id", validators=[DataRequired()])
    comment = TextAreaField("comment", validators=[DataRequired()])
