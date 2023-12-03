from flask import Blueprint, render_template

from app.models import Gallery

bp = Blueprint('gallery', __name__, url_prefix='/gallery')


@bp.route('/list/')
def _list():
    gall_list = Gallery.query.order_by(Gallery.create_date.desc())
    return render_template('gallery/gall_list.html', gall_list=gall_list)


@bp.route('/detail/<int:id>/')
def detail(id):
    gallery = Gallery.query.get_or_404(id)
    return render_template('gallery/gall_content_detail.html', gallery=gallery)
