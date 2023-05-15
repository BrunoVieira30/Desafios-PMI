from flask import Flask, render_template, url_for
import mysql.connector

app = Flask(__name__)

# MySQL
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

cursor = database.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS desafio3")
cursor.execute("USE desafio3")

@app.route('/')
def index():
    return render_template('index.html', background= url_for('static', filename='imagens/fundo.png'))

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    return render_template('contato.html', background= url_for('static', filename='imagens/fundo2.png'))

@app.route('/quemsomos')
def quemsomos():
    return render_template('quem_somos.html', background= url_for('static', filename='imagens/fundo2.png'))

app.run(debug=True)