from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def hello_world():
    return "hello wor"


@bp.route('/hello')
def hello():
    return "heLLO"
