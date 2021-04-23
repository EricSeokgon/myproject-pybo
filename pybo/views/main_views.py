from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def helo_pybo():
    return 'Hello, pybo!'


@bp.route('/')
def index():
    return 'Pybo index'
