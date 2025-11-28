from . import db

class Curso(db.Model):
    __tablename__ = 'cursos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), unique=True, index=True)
    descricao = db.Column(db.String(250))

    def __repr__(self):
        return '<Curso %r>' % self.nome
