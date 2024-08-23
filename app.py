from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração da base de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meu_banco_de_dados.db'
db = SQLAlchemy(app)

# Definindo o modelo da base de dados
class Dados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(50), nullable=False)
    valor = db.Column(db.Float, nullable=False)

@app.route('/dashboard')
def dashboard():
    # Consultando os dados na base de dados
    dados = Dados.query.all()

    # Preparando os dados para o dashboard
    categorias = [dado.categoria for dado in dados]
    valores = [dado.valor for dado in dados]

    return render_template('dashboard.html', categorias=categorias, valores=valores)

@app.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    dados = Dados(categoria=data['categoria'],
                  valor=data['valor'])
    db.session.add(dados)
    db.session.commit()
    return jsonify({'messege':'Dado criado com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)
