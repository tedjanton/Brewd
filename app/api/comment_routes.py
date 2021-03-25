from app.models import db, Comment
from flask_login import login_required
from flask import Blueprint, session, request
from app.forms import CommentForm

comment_routes = Blueprint("comment_routes", __name__)


@comment_routes.route('/', methods=["POST"])
@login_required
def add_comment():
    " ADD A COMMENT TO THE DB "
    form = CommentForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    print("info", form.user_id.data, form.sip_id.data, form.comment.data)
    if form.validate_on_submit():
        new_comment = Comment(user_id=form.user_id.data,
                              sip_id=form.sip_id.data,
                              comment=form.comment.data)
        print("NEW COMMENT", new_comment)
        db.session.add(new_comment)
        db.session.commit()
        return new_comment.to_dict()
    else:
        return {"errors": "invalid submission"}
