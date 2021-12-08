import pytest
from FlaskTask import create_app


@pytest.fixture
def client():
    app = create_app({'TESTING': True})
    client = app.test_client()
    return client


cases = [
    ('/', 302, b'Redirecting...'),
    ('/report/', 200, b'Drivers report'),
    ('/report/drivers/', 200, b'Drivers list'),
    ('/report/drivers/?driver_id=SVF', 200, b'Drivers report'),
    ('/report/drivers/?order=desc', 200, b'Drivers list')
]


@pytest.mark.parametrize('param,expected,expected_tittle', cases)
def test_urls(client, param, expected, expected_tittle):
    rv = client.get(param)
    assert rv.status_code == expected
    assert expected_tittle in rv.data


def test_post(client):
    with client.get('/report/drivers/?driver_id=SVF') as rv:
        assert rv.request.args['driver_id'] == 'SVF'
        assert rv.request.path == '/report/drivers/'
    with client.get('/?order=desc') as rv:
        assert rv.request.args['order'] == 'desc'
        assert rv.request.path == '/'
