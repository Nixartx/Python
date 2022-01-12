from FlaskSQL.models import *
from FlaskSQL.generate import *
from FlaskSQL.config import Config
from flask import Flask


def add_groups_db(groups):
    # Add groups to DB
    for group in groups:
        db.session.add(Group(name=group))
    db.session.commit()


def add_students_db(students, groups_students):
    # Add students to DB
    for student in students:
        # Find students group
        gr_name = None
        for group in groups_students:
            if student in groups_students[group]:
                gr_name = group
        gr = Group.query.filter_by(name=gr_name).first()
        gr_id = gr.id if gr else gr
        fn, ln = student.split(' ')
        db.session.add(
            Student(
                first_name=fn,
                last_name=ln,
                group_id=gr_id))
    db.session.flush()


def add_course_db(students):
    courses_students = course_assign(students)
    for course in courses_students:
        st_list = []
        for student in courses_students[course]:
            fn, ln = student.split(' ')
            st = Student.query.filter_by(
                first_name=fn, last_name=ln).first()
            st_list.append(st)
        db.session.add(Course(name=course, students=st_list))
    db.session.flush()


def create_data(dbpath=None):
    app = Flask(__name__)
    dbpath = dbpath if dbpath else Config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_DATABASE_URI'] = dbpath
    db.init_app(app)
    app.app_context().push()
    db.create_all()
    students = student_name(200)
    groups = group_name(10)
    groups_students, free_students, free_groups = group_assign(
        groups, students)

    add_groups_db(groups)
    add_students_db(students, groups_students)
    add_course_db(students)

    db.session.commit()
    db.session.remove()
    return 'Data added'


def drop():
    db.session.remove()
    db.drop_all()
    return 'Tables is reset'
