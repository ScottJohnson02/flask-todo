import pytest
import psycopg2


from flasktodo.db import get_db
from flasktodo import db
from flask import g, session


# test the login feature


def test_login(client, email='test', password='test'):
    client.post(
        '/login',
        data={'email': email, 'password': password})
    response = client.get('/')
    assert b'Welcome test' in response.data

# validate user input


@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('a', 'test', b'Incorrect email.'),
    ('test', 'a', b'Incorrect password.'),
))
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    assert message in response.data

# test logging out user


def test_logout(client, auth):
    auth.login()

    with client:
        auth.logout()
        assert 'user_id' not in session
