from flasky import app, db

# Script para criar o banco de dados manualmente
with app.app_context():
    db.create_all()
    print("Banco de dados inicializado e tabelas criadas com sucesso!")
