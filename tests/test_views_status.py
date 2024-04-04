from flask import url_for


def test_app(client):
    assert client.get(url_for("user1.contact")).status_code == 200
