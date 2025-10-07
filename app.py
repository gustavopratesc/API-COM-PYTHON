# API - É um lugar para disponibilizar recursos ou funcionalidades
# 1 - Objetivo - Criar uma API de disponibiliza a consulta, criação, edição e exclusão de livros.
# 2 - URL base - localhost
# 3 - Endpoints -
    # - localhost/livros (GET)
    # - localhost/livros/id (GET)
    # - localhost/livros/id (PUT)
    # - localhost/livros/id (DELETE)
# 4 Quais recursos - Livros

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O Senhor dos Aneis - A sociedade do Anel',
        'autor': 'J.R.R Tolkien' 
    },
    {
        'id': 2,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id': 3,
        'Titulo': 'James Clear',
        'autor': 'Habitos Atômicos'
    },
]

#OBTER
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

#OBTER POR ID
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        
#EDITAR
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for i, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[i].update(livro_alterado)
            return jsonify(livros[i])
#CRIAR
@app.route('/livros', methods=['POST'])        
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

#DELETAR
@app.route('/livros/<int:id>', methods=['DELETE'])
def deletar_livro(id):
    for i, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[i]
    return jsonify(livros)

app.run(port=5000, host='localhost', debug=True)