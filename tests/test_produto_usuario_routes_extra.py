import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from types import SimpleNamespace

import pytest

import views.produto as produto_view
import views.usuario as usuario_view
from app import app as flask_app


@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    flask_app.config["WTF_CSRF_ENABLED"] = False

    with flask_app.test_client() as client:
        yield client


def login(client):
    with client.session_transaction() as sess:
        sess["logged"] = True


@pytest.mark.parametrize(
    ("idproduto", "esperado"),
    [
        ("1", True),
        ("0", False),
        ("", False),
        ("abc", False),
        (None, False),
    ],
)
def test_idproduto_valido(idproduto, esperado):
    assert produto_view.idproduto_valido(idproduto) is esperado


@pytest.mark.parametrize(
    ("nome", "quantidade", "categoria", "mensagem"),
    [
        ("", "1", "Informática", produto_view.MSG_NOME_INVALIDO),
        ("A" * 41, "1", "Informática", produto_view.MSG_NOME_INVALIDO),
        ("Mouse", "", "Informática", produto_view.MSG_QUANTIDADE_INVALIDA),
        ("Mouse", "abc", "Informática", produto_view.MSG_QUANTIDADE_INVALIDA),
        ("Mouse", "-1", "Informática", produto_view.MSG_QUANTIDADE_INVALIDA),
        ("Mouse", "1", "", produto_view.MSG_CATEGORIA_INVALIDA),
        ("Mouse", "1", "Outra", produto_view.MSG_CATEGORIA_INVALIDA),
        ("Mouse", "1", "Informática", None),
    ],
)
def test_validar_dados_produto(nome, quantidade, categoria, mensagem):
    assert produto_view.validar_dados_produto(nome, quantidade, categoria) == mensagem


class ProdutoFake:
    produto = SimpleNamespace(
        idproduto=1,
        nome="Mouse",
        quantidade=10,
        categoria="Informática",
    )

    def insert(self, request):
        return None

    def delete(self, request):
        return None

    def edit(self, request):
        return None

    def list(self, request):
        return [self.produto]

    def view(self, request):
        return self.produto


class ProdutoFakeNaoEncontrado(ProdutoFake):
    def view(self, request):
        return None


def test_insert_get_logado_renderiza_formulario(client):
    login(client)

    response = client.get("/main/produtos/insert")

    assert response.status_code == 200


def test_insert_post_invalido_renderiza_formulario(client):
    login(client)

    response = client.post(
        "/main/produtos/insert",
        data={"nome": "", "quantidade": "1", "categoria": "Informática"},
    )

    assert response.status_code == 200


def test_insert_post_valido_renderiza_formulario(client, monkeypatch):
    login(client)
    monkeypatch.setattr(produto_view, "Produto", ProdutoFake)

    response = client.post(
        "/main/produtos/insert",
        data={"nome": "Mouse", "quantidade": "1", "categoria": "Informática"},
    )

    assert response.status_code == 200


def test_list_logado_renderiza_lista(client, monkeypatch):
    login(client)
    monkeypatch.setattr(produto_view, "Produto", ProdutoFake)

    response = client.get("/main/produtos")

    assert response.status_code == 200


def test_delete_com_id_invalido_redireciona(client):
    login(client)

    response = client.post("/main/produtos/delete", data={"idproduto": "abc"})

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/main/produtos")


def test_delete_produto_nao_encontrado_redireciona(client, monkeypatch):
    login(client)
    monkeypatch.setattr(produto_view, "Produto", ProdutoFakeNaoEncontrado)

    response = client.post("/main/produtos/delete", data={"idproduto": "1"})

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/main/produtos")


def test_delete_valido_redireciona(client, monkeypatch):
    login(client)
    monkeypatch.setattr(produto_view, "Produto", ProdutoFake)

    response = client.post("/main/produtos/delete", data={"idproduto": "1"})

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/main/produtos")


def test_edit_get_id_invalido_redireciona(client):
    login(client)

    response = client.get("/main/produtos/edit?idproduto=abc")

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/main/produtos")


def test_edit_get_produto_nao_encontrado_redireciona(client, monkeypatch):
    login(client)
    monkeypatch.setattr(produto_view, "Produto", ProdutoFakeNaoEncontrado)

    response = client.get("/main/produtos/edit?idproduto=1")

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/main/produtos")


def test_edit_get_valido_renderiza_formulario(client, monkeypatch):
    login(client)
    monkeypatch.setattr(produto_view, "Produto", ProdutoFake)

    response = client.get("/main/produtos/edit?idproduto=1")

    assert response.status_code == 200


def test_edit_post_id_invalido_redireciona(client):
    login(client)

    response = client.post(
        "/main/produtos/edit",
        data={"idproduto": "abc", "nome": "Mouse", "quantidade": "1", "categoria": "Informática"},
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/main/produtos")


def test_edit_post_dados_invalidos_renderiza_formulario(client):
    login(client)

    response = client.post(
        "/main/produtos/edit",
        data={"idproduto": "1", "nome": "", "quantidade": "1", "categoria": "Informática"},
    )

    assert response.status_code == 200


def test_edit_post_produto_nao_encontrado_redireciona(client, monkeypatch):
    login(client)
    monkeypatch.setattr(produto_view, "Produto", ProdutoFakeNaoEncontrado)

    response = client.post(
        "/main/produtos/edit",
        data={"idproduto": "1", "nome": "Mouse", "quantidade": "1", "categoria": "Informática"},
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/main/produtos")


def test_edit_post_valido_renderiza_formulario(client, monkeypatch):
    login(client)
    monkeypatch.setattr(produto_view, "Produto", ProdutoFake)

    response = client.post(
        "/main/produtos/edit",
        data={"idproduto": "1", "nome": "Mouse", "quantidade": "1", "categoria": "Informática"},
    )

    assert response.status_code == 200


def test_index_logado_redireciona_para_main(client):
    login(client)

    response = client.get("/")

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/main")


def test_main_logado_renderiza_pagina(client):
    login(client)

    response = client.get("/main")

    assert response.status_code == 200


class UsuarioFakeSemRegistro:
    def login(self, request):
        return None


class UsuarioFakeComRegistro:
    def login(self, request):
        return SimpleNamespace(senha="hash")


def test_login_usuario_inexistente_renderiza_index(client, monkeypatch):
    monkeypatch.setattr(usuario_view, "Usuario", UsuarioFakeSemRegistro)

    response = client.post("/login", data={"usuario": "admin", "senha": "123"})

    assert response.status_code == 200


def test_login_senha_invalida_renderiza_index(client, monkeypatch):
    monkeypatch.setattr(usuario_view, "Usuario", UsuarioFakeComRegistro)
    monkeypatch.setattr(usuario_view, "checkpw", lambda senha, hash_senha: False)

    response = client.post("/login", data={"usuario": "admin", "senha": "123"})

    assert response.status_code == 200


def test_login_valido_redireciona_para_main(client, monkeypatch):
    monkeypatch.setattr(usuario_view, "Usuario", UsuarioFakeComRegistro)
    monkeypatch.setattr(usuario_view, "checkpw", lambda senha, hash_senha: True)

    response = client.post("/login", data={"usuario": "admin", "senha": "123"})

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/main")


def test_logout_limpa_sessao_e_redireciona(client):
    login(client)

    response = client.get("/logout")

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/")
