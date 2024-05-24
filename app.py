from flask import Flask, jsonify, request

# Criando aplicação Flask com nome atual
app = Flask(__name__)
# Fonte de dados na lista de dicionários
livros = [
    {
        'id': 1,
        'Título': "Código limpo",
        'autor': 'Robert C. Martin'
    },
    {
        'id': 2,
        'Título': 'Introdução a Programação Python',
        'autor': 'Nilo Ney Coutinho Menezes'
    },
    {
        'id': 3,
        'Título': 'Entendendo Algoritmos',
        'autor': 'Aditya Y. Bhargava',
    },
]


# Consultar (todos livros) e especificando que seja aceita apenas o método GET
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)


# Consultar(id) <> especifica que o número esperado seja inteiro e será
# identificado com a palavra chave 'id'
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livo_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)


# Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    # retorna as informações que foram enviadas do usuário para a api
    livro_alerado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alerado)
            return jsonify(livros[indice])


# Incluir novo livro
# Método POST permite criar algo
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)


# Exclir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)


# Iniciando a aplicação
app.run(port=5000, host='localhost', debug=True)
