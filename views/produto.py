from flask import request, render_template, url_for, redirect, flash
from app import app

from models.Produto import Produto

CATEGORIAS_VALIDAS = [
    'Informática',
    'Telefonia',
    'Moda',
    'Eletrodomésticos',
    'Automotivo',
    'Pet Shop',
]

MSG_IDPRODUTO_INVALIDO = "Campo 'idproduto' é obrigatório e deve ser numérico."
MSG_NOME_INVALIDO = "Campo 'nome' é obrigatório e deve ter no máximo 40 caracteres."
MSG_QUANTIDADE_INVALIDA = "Campo 'quantidade' é obrigatório e deve ser numérico."
MSG_CATEGORIA_INVALIDA = "Campo 'categoria' é obrigatório ou é inválido."


def idproduto_valido(idproduto):
    return bool(idproduto and idproduto.isdigit() and int(idproduto) > 0)


def validar_dados_produto(nome, quantidade, categoria):
    if not nome or len(nome) > 40:
        return MSG_NOME_INVALIDO

    if not quantidade or not quantidade.isdigit() or int(quantidade) < 0:
        return MSG_QUANTIDADE_INVALIDA

    if not categoria or categoria not in CATEGORIAS_VALIDAS:
        return MSG_CATEGORIA_INVALIDA

    return None


@app.route('/main/produtos/insert', methods=['GET', 'POST'], endpoint='produto.insert')
def insert():
    if request.method == 'GET':
        return render_template('produtos/insert.html')

    else:
        nome = request.form.get('nome', '')
        quantidade = request.form.get('quantidade', '')
        categoria = request.form.get('categoria', '')

        erro = validar_dados_produto(nome, quantidade, categoria)

        if erro:
            flash(erro)

        else:
            model = Produto()
            model.insert(request)
            flash('Produto inserido com sucesso.')

        return render_template('produtos/insert.html')


@app.route('/main/produtos/delete', methods=['GET'], endpoint='produto.delete')
def delete():
    idproduto = request.values.get('idproduto', '')

    if not idproduto_valido(idproduto):
        flash(MSG_IDPRODUTO_INVALIDO)

    else:
        model = Produto()
        model.delete(request)
        flash('Produto excluído com sucesso.')

    return redirect(url_for('produto.list'))


@app.route('/main/produtos', methods=['GET'], endpoint='produto.list')
def list():
    model = Produto()
    produtos = model.list(request)
    return render_template('produtos/list.html', produtos=produtos)


@app.route('/main/produtos/edit', methods=['GET', 'POST'], endpoint='produto.edit')
def edit():
    if request.method == 'GET':
        idproduto = request.values.get('idproduto', '')

        if not idproduto_valido(idproduto):
            flash(MSG_IDPRODUTO_INVALIDO)
            return redirect(url_for('produto.list'))

        else:
            model = Produto()
            produto = model.view(request)
            return render_template('produtos/edit.html', produto=produto)

    else:
        idproduto = request.form.get('idproduto', '')
        nome = request.form.get('nome', '')
        quantidade = request.form.get('quantidade', '')
        categoria = request.form.get('categoria', '')

        erro = validar_dados_produto(nome, quantidade, categoria)

        if not idproduto_valido(idproduto):
            flash(MSG_IDPRODUTO_INVALIDO)

        elif erro:
            flash(erro)

        else:
            model = Produto()
            model.edit(request)
            flash('Produto alterado com sucesso.')

        return render_template('produtos/edit.html', produto=request.form)
