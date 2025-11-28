from flask import render_template, redirect, url_for, flash
from . import bp
from .forms import CursoForm
from .. import db
from ..models import Curso
from datetime import datetime

# Rota Principal
@bp.route('/')
def index():
 
    aluno = "Rogério Santos Barbosa"
    prontuario = "PT3032051"
    return render_template('index.html', 
                           aluno=aluno, 
                           prontuario=prontuario, 
                           current_time=datetime.utcnow())

# Rota de Cadastro de Cursos
@bp.route('/cursos', methods=['GET', 'POST'])
def cursos():
    form = CursoForm()
    if form.validate_on_submit():
        # Verifica duplicidade
        curso_existente = Curso.query.filter_by(nome=form.nome.data).first()
        if curso_existente:
            flash('Atenção: Este curso já está cadastrado.', 'warning')
        else:
            novo_curso = Curso(nome=form.nome.data, descricao=form.descricao.data)
            db.session.add(novo_curso)
            db.session.commit()
            flash('Curso cadastrado com sucesso!', 'success')
            return redirect(url_for('main.cursos'))
            
    # Listagem de cursos
    lista_cursos = Curso.query.all()
    return render_template('cursos.html', form=form, cursos=lista_cursos, current_time=datetime.utcnow())

# Rotas Não Disponíveis
@bp.route('/professores')
@bp.route('/disciplinas')
@bp.route('/alunos')
@bp.route('/ocorrencias')
def nao_disponivel():
    return render_template('nao_disponivel.html', current_time=datetime.utcnow())
