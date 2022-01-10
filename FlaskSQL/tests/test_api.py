import pytest
import requests
from FlaskSQL.app import create_app


@pytest.fixture
def client():
    app = create_app({'TESTING': True})
    app.app_context().push()
    app.test_client().get('http://localhost:5000/fill')
    with app.test_client() as client:
        yield client
    app.test_client().get('http://localhost:5000/drop')


def test_find_groups(client):
    result = client.get('http://localhost:5000/groups/15')
    assert result.status_code == 200


def test_find_course(client):
    result = client.get('http://localhost:5000/course/Math')
    assert result.status_code == 200


def test_add_delete_student(client):
    result = client.post(
        'http://localhost:5000/student',
        data={
            'first_n': 'Adam',
            'last_n': 'Jensen'})
    assert result.status_code == 200
    st_id = result.get_json()
    result = client.delete('http://localhost:5000/student', data={'id': st_id})
    assert result.status_code == 200
    assert result.get_json() == st_id


def test_add_delete_course_to_student(client):
    client.post(
        'http://localhost:5000/student',
        data={
            'first_n': 'Adam',
            'last_n': 'Jensen'})
    result = client.post(
        'http://localhost:5000/course',
        data={
            'first_n': 'Adam',
            'last_n': 'Jensen',
            'course': 'Math'})
    assert result.status_code == 200
    course_id = result.get_json()
    result = client.delete(
        'http://localhost:5000/course',
        data={
            'first_n': 'Adam',
            'last_n': 'Jensen',
            'course': 'Math'})
    assert result.status_code == 200
    assert result.get_json() == course_id
