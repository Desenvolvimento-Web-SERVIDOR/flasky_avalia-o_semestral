from flask import render_template
from . import bp

@bp.app_errorhandler(404)
def page_not_found(e):
    # Em um cenário real, teríamos um template 404.html. 
    # Aqui usamos o base com uma mensagem simples para não quebrar.
    return render_template('base.html'), 404

@bp.app_errorhandler(500)
def internal_server_error(e):
    return render_template('base.html'), 500
