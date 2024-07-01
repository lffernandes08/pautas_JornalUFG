from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

pautas = []

@app.context_processor
def utility_processor():
    def custom_enumerate(sequence):
        return enumerate(sequence)
    return dict(enumerate=custom_enumerate)

@app.route('/')
def index():
    return render_template('index.html', pautas=pautas)

@app.route('/add_pauta', methods=['POST'])
def add_pauta():
    reporter = request.form['reporter']
    descricao = request.form['descricao']
    fonte = request.form['fonte']
    unidade = request.form['unidade']
    telefone = request.form['telefone']
    data_inicio = request.form['data_inicio']
    previsao_entrega = request.form['previsao_entrega']

    pauta = {
        'reporter': reporter,
        'descricao': descricao,
        'fonte': fonte,
        'unidade': unidade,
        'telefone': telefone,
        'data_inicio': datetime.strptime(data_inicio, '%Y-%m-%d').strftime('%d/%m/%Y'),
        'previsao_entrega': datetime.strptime(previsao_entrega, '%Y-%m-%d').strftime('%d/%m/%Y')
    }

    pautas.append(pauta)
    return redirect(url_for('index'))

@app.route('/delete_pauta/<int:index>', methods=['POST'])
def delete_pauta(index):
    if 0 <= index < len(pautas):
        pautas.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
