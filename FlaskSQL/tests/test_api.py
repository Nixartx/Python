import pytest
import sqlalchemy

from FlaskSQL.initdb import create_data, drop
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from FlaskSQL.app import create_app
from FlaskSQL.models import *

testdb_path = 'postgresql://postgres:admin@localhost/schedule_test'
engine = create_engine(testdb_path)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_student_to_db(f_name, l_name):
    student = Student(first_name=f_name, last_name=l_name)
    session.add(student)
    session.commit()
    st_id = student.id
    session.close()
    return st_id


def find_schedule_first():
    sql = sqlalchemy.text('SELECT * FROM schedule LIMIT 1')
    result = {}
    for row in session.execute(sql):
        result = {
            'student_id': row['student_id'],
            'course_id': row['course_id']}
        session.close()
    return result


@pytest.fixture
def client():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': testdb_path})
    create_data(testdb_path)
    with app.test_client() as client:
        yield client
    drop()


def test_find_groups(client):
    result = client.get('/groups?students_number=15')
    sql = sqlalchemy.text(
        '''
        SELECT COUNT(students.id)
        FROM "groups"
        JOIN students ON students.group_id = "groups".id
        GROUP BY students.group_id
        HAVING count(students.id) <= 15
        ''')
    r = []
    for row in session.execute(sql):
        r.append(row)
    session.close()
    assert len(result.get_json()) == len(r)
    assert result.status_code == 200


def test_find_course(client):
    sql = sqlalchemy.text(
        ''' SELECT * FROM schedule
            JOIN students ON students.id = schedule.student_id
            JOIN courses ON courses.id = schedule.course_id
            WHERE courses.name = 'Math'
            ''')
    r = []
    for row in session.execute(sql):
        r.append(row)
    session.close()
    result = client.get('/course?course_name=Math')
    assert result.status_code == 200
    assert len(result.get_json()) == len(r)


def test_add_student(client):
    result = client.post(
        '/student',
        data={
            'first_n': 'Adam',
            'last_n': 'Jensen'})
    assert result.status_code == 201
    st = result.get_json()
    assert st['first_name'] == 'Adam'
    assert st['last_name'] == 'Jensen'


def test_delete_student_suc(client):
    st_id = add_student_to_db('Adam', 'Jensen')
    result = client.delete('/student/{}'.format(st_id))
    check_st = session.query(Student).filter_by(id=st_id).first()
    session.close()
    assert check_st is None
    assert result.status_code == 204


def test_delete_student_er(client):
    result = client.delete('/student/999')
    assert result.status_code == 204


def test_add_course_to_student(client):
    st = add_student_to_db('Adam', 'Jensen')
    courses_list = [1, 2, 3]
    result = client.post(
        '/student/{}/courses'.format(st), data={'courses_list': courses_list})
    assert result.status_code == 201


def test_delete_course_to_student(client):
    schedule = find_schedule_first()
    result = client.delete(
        '/student/{}/course/{}'.format(schedule['student_id'], schedule['course_id']))
    assert result.status_code == 204
    assert schedule != find_schedule_first()
