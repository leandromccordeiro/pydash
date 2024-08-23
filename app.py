# from flask import Flask, jsonify, render_template, request
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# # Configuração da base de dados
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meu_banco_de_dados.db'
# db = SQLAlchemy(app)

# # Definindo o modelo da base de dados
# class Dados(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     categoria = db.Column(db.String(50), nullable=False)
#     valor = db.Column(db.Float, nullable=False)

# @app.route('/dashboard')
# def dashboard():
#     # Consultando os dados na base de dados
#     dados = Dados.query.all()

#     # Preparando os dados para o dashboard
#     categorias = [dado.categoria for dado in dados]
#     valores = [dado.valor for dado in dados]

#     return render_template('dashboard.html', categorias=categorias, valores=valores)

# @app.route('/create', methods=['POST'])
# def create():
#     data = request.get_json()
#     dados = Dados(categoria=data['categoria'],
#                   valor=data['valor'])
#     db.session.add(dados)
#     db.session.commit()
#     return jsonify({'messege':'Dado criado com sucesso!'})

# if __name__ == '__main__':
#     app.run(debug=True)



import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# Inicializando o app Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Simulando dados de uma base de dados
data = {
    'Categoria': ['A', 'B', 'C', 'D'],
    'Valor': [100, 200, 300, 400]
}
df = pd.DataFrame(data)

# Criando um gráfico com Plotly
fig = px.bar(df, x='Categoria', y='Valor', title='Valores por Categoria')

# Layout do Dashboard
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Meu Dashboard", className='text-center mb-4'), width=12)
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig), width=12)
    ]),
    dbc.Row([
        dbc.Col(html.P("Este é um exemplo de dashboard criado com Dash e Plotly.", className='text-center mt-4'), width=12)
    ])
], fluid=True)

# Executando o servidor
if __name__ == '__main__':
    app.run_server(debug=True)
