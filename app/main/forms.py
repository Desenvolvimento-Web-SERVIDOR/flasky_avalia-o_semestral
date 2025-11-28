from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class CursoForm(FlaskForm):
    nome = StringField('Qual é o nome do curso?', validators=[DataRequired()])
    descricao = TextAreaField('Descrição (250 caracteres)', validators=[
        DataRequired(), 
        Length(max=250, message="Máximo de 250 caracteres")
    ])
    submit = SubmitField('Cadastrar')
