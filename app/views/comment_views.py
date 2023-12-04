from datetime import datetime

from flask import Blueprint, url_for, request
from werkzeug.utils import redirect

from app import db
from app.models import Gallery, Comment

bp = Blueprint('comment', __name__, url_prefix='/comment')


@bp.route('/create/<int:id>', methods=('POST',))
def create(id):
    gall = Gallery.query.get_or_404(id)
    content = request.form["content"]
    comment = Comment(content=content, create_date=datetime.now())
    gall.comment_set.append(comment)
    db.session.commit()
    return redirect(url_for('gallery.detail', id=id))
