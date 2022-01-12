import pytest
from FlaskSQL.initdb import create_data, drop
import requests
from FlaskSQL.app import create_app


@pytest.fixture
def client():
    testdb_path = 'postgresql://postgres:admin@localhost/PostgreDBtest'
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': testdb_path})
    create_data(testdb_path)
    with app.test_client() as client:
        yield client
    drop()


def test_find_groups(client):
    result = client.get('/groups/15')
    assert len(result.get_json()) >= 1
    assert result.status_code == 200


def test_find_course(client):
    result = client.get('/course/Math')
    assert result.status_code == 200


def test_add_student(client):
    result = client.post('/student/Adam Jensen')
    assert result.status_code == 201
    st = result.get_json()
    assert st['first_name'] == 'Adam'
    assert st['last_name'] == 'Jensen'


def test_delete_student(client):
    result = client.delete('/student/1')
    assert result.status_code == 204
    result = client.delete('/student/999')
    assert result.status_code == 403


def test_add_course_to_student(client):
    result = client.post('/student/Adam Jensen')
    st = result.get_json()
    result = client.get('/course/Math')
    c = result.get_json()
    result = client.post(
        '/students/{}/courses/{}'.format(st['id'], c[0]['course_id']))
    assert result.status_code == 201


def test_delete_course_to_student(client):
    student_id = 200
    while student_id:
        result = client.delete('/students/{}/courses/1'.format(student_id))
        if result.status_code == 204:
            assert result.status_code == 204
            student_id = 0
        else:
            assert result.status_code == 403
            student_id -= 1
