import pytest
import psycopg2


from flasktodo.db import get_db


def test_todo_list(client):
    # View the home page and check to see the header and a to-do item
    response = client.get('/')
    assert b'<h1>A simple to-do application</h1>' in response.data
    assert b'clean room' in response.data

    # Mock data should show three to-do items, one of which is complete
    assert response.data.count(b'<li class="">') == 2
    assert response.data.count(b'<li class="completed">') == 1


def test_new_todo(client,):
    response = client.post(
        '/',
        data={'task': "tie shoes"}
    )
    assert response.data.count(b'<li class="">') == 3


def test_complete_todo(client,):
    response = client.get(
        '/1/done',
    )
    assert response.data == 1
