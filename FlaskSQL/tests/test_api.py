import pytest
from FlaskSQL.initdb import create_data, drop
from sqlalchemy import MetaData, Table, create_engine
from FlaskSQL.app import create_app

testdb_path = 'postgresql://postgres:admin@localhost/schedule_test'


def add_student_to_db(f_name, l_name):
    engine = create_engine(testdb_path)
    metadata = MetaData()
    students = Table('students', metadata, autoload=True, autoload_with=engine)
    st_ins = students.insert().values(
        first_name=f_name,
        last_name=l_name).returning(
        students.columns.id)
    con = engine.connect()
    st_id = None
    for row in con.execute(st_ins):
        st_id = row['id']
    return st_id


def find_schedule_first():
    engine = create_engine(testdb_path)
    metadata = MetaData()
    schedules = Table(
        'schedule',
        metadata,
        autoload=True,
        autoload_with=engine)
    schedule = schedules.select()
    con = engine.connect()
    result = None
    for row in con.execute(schedule):
        result = {
            'student_id': row['student_id'],
            'course_id': row['course_id']}
        break
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
    assert len(result.get_json()) >= 1
    assert result.status_code == 200


def test_find_course(client):
    result = client.get('/course?course_name=Math')
    assert result.status_code == 200


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
    assert result.status_code == 204


def test_delete_student_er(client):
    result = client.delete('/student/999')
    assert result.status_code == 404


def test_add_course_to_student(client):
    st = add_student_to_db('Adam', 'Jensen')
    courses_list = ['Math', 'Biology', 'Chemistry']
    result = client.post(
        '/student/{}/courses'.format(st), data={'courses_list': courses_list})
    assert result.status_code == 201


def test_delete_course_to_student(client):
    schedule = find_schedule_first()
    result = client.delete(
        '/student/{}/course/{}'.format(schedule['student_id'], schedule['course_id']))
    assert result.status_code == 204
    assert schedule != find_schedule_first()
