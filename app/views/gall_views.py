from datetime import datetime
from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect
from app import db
from app.models import Gallery
from app.forms import GalleryForm

bp = Blueprint('gallery', __name__, url_prefix='/gallery')


@bp.route('/list/')
def _list():
    gall_list = Gallery.query.order_by(Gallery.create_date.desc())
    return render_template('gallery/gall_list.html', gall_list=gall_list)


@bp.route('/detail/<int:id>/')
def detail(id):
    gallery = Gallery.query.get_or_404(id)
    return render_template('gallery/gall_content_detail.html', gallery=gallery)


@bp.route('/create/', methods=('GET', 'POST'))
def create():
    form = GalleryForm()
    if request.method == 'POST' and form.validate_on_submit():
        gallery = Gallery(title=form.title.data,
                          content=form.content.data, create_date=datetime.now())
        db.session.add(gallery)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('gallery/gall_form.html', form=form)
