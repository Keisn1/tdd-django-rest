from django.urls import reverse

from drf_project.views import ping


def test_ping(client):
    resp = client.get(reverse(ping))
    assert resp.json() == {"ping": "pong"}
