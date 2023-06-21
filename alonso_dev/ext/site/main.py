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

@bp.route('/jogo_da_velha')
def jogo_velha():
    return render_template('jogo_velha.html')

@bp.route('/sobre')
def sobre():
    return render_template('sobre.html')

@bp.route('/melhores_jogos_do_mundo')
def jogos():
    return render_template('jogos.htlm')

@bp.route('/testes')
def teste():
    return render_template('testes.html')