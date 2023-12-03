from flask import Blueprint, url_for
from werkzeug.utils import redirect

from app.models import Gallery

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    return redirect(url_for('gallery._list'))
