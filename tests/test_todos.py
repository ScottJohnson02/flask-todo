import pytest
import psycopg2


from flasktodo.db import get_db
from flasktodo import db
from flask import g, session


def test_todo_list(client, auth):
    # View the home page and check to see the header and a to-do item
    auth.login()
    response = client.get('/')
    assert b'<h1>A simple to-do application</h1>' in response.data

    # Mock data should show three to-do items, one of which is complete
    assert response.data.count(b'<li class="">') == 2
    assert response.data.count(b'<li class="completed">') == 1


def test_new_todo(client, auth):
    auth.login()
    response = client.post(
        '/',
        data={'task': "tie shoes"}
    )
    assert response.data.count(b'<li class="">') == 3


def test_completed(client, auth):
    # View the home page and check to see the header and a completed items
    auth.login()
    response = client.get('/completed')
    assert b'clean room' not in response.data

    # Mock data should show completed items
    assert response.data.count(b'<li class="completed">') == 1


def test_uncompleted(client, auth):
    auth.login()
    # View the home page and check to see the header uncompleted items
    response = client.get('/uncompleted')
    assert b'clean room' in response.data

    # Mock data should show uncompleted items
    assert response.data.count(b'<li class="completed">') == 0


def test_marked(client, auth):
    # goes to the page where the user marks a task complete
    auth.login()
    client.post(
        '/1/done',
    )
    response = client.get(
        '/',
    )
    # checks the number of completed tasks
    assert response.data.count(b'<li class="">') == 1
    assert response.data.count(b'<li class="completed">') == 2


def test_delete(client, auth):
    auth.login()
    client.post(
        '/1/delete',
    )
    response = client.get(
        '/',
    )

    assert response.data.count(b'<li class="">') == 1


def test_edit(client, auth):
    # goes to the update tasks page
    auth.login()
    client.post(
        '/1/edit',
        data={'new': "tie shoes"}
    )
    response = client.get('/')
    # checks that the edit went through and did not add a task
    assert b'tie shoes' in response.data
    assert response.data.count(b'<li class="">') == 2
