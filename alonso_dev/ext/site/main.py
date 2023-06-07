from flask import Blueprint, render_template


bp = Blueprint("site", __name__)


@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/tag')
def tag():
    return render_template('tags.html')

@bp.route('/tarefas')
def tarefas():
    return render_template('tarefas.html')