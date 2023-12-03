from datetime import datetime

from flask import Blueprint, url_for, request
from werkzeug.utils import redirect

from app import db
from app.models import Gallery

bp = Blueprint('coment', __name__, url_prefix='/coment')


@bp.route('/create/<int:id>', methods=('POST',))
def create(id):
    gall = Gallery.query.get_or_404(id)
    content = request.form("content")
    coment
