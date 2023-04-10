from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', background= url_for('static', filename='imagens/fundo.png'))

@app.route('/contato')
def contato():
    return render_template('contato.html', background= url_for('static', filename='imagens/fundo2.png'))

@app.route('/quemsomos')
def quemsomos():
    return render_template('quem_somos.html', background= url_for('static', filename='imagens/fundo2.png'))

app.run(debug=True)