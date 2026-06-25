import pytest

from app import app as flask_app


@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    flask_app.config["WTF_CSRF_ENABLED"] = False

    with flask_app.test_client() as client:
        yield client


def test_index_returns_200_when_not_logged_in(client):
    response = client.get("/")

    assert response.status_code == 200


def test_main_redirects_when_not_logged_in(client):
    response = client.get("/main")

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/")


@pytest.mark.parametrize(
    ("method", "path", "data"),
    [
        ("get", "/main/produtos", None),
        ("get", "/main/produtos/insert", None),
        ("get", "/main/produtos/edit?idproduto=1", None),
        ("post", "/main/produtos/delete", {"idproduto": "1"}),
    ],
)
def test_product_routes_redirect_when_not_logged_in(client, method, path, data):
    request_method = getattr(client, method)
    response = request_method(path, data=data)

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/")
