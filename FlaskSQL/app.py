from flask import Flask, make_response, request
import os
import json
from FlaskSQL.models import *
from FlaskSQL.schema import *
from flask_restful import Resource, Api
from FlaskSQL.generate import *


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object('FlaskSQL.config.Config')
    else:
        # load the test config if passed in
        app.config.from_object('FlaskSQL.tests.test_config.Config')

    db.init_app(app)
    api = Api(app)

    # Marshmallow schema
    group_schema = GroupSchema(many=True)
    schedule_schema = ScheduleSchema(many=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Populate the database
    class CreateData(Resource):
        def get(self):
            db.create_all()
            students = student_name(200)
            groups = group_name(10)
            groups_students, free_students, free_groups = group_assign(
                groups, students)
            courses_students = course_assign(students)

            # Add groups to DB
            for group in groups:
                db.session.add(Group(name=group))
            db.session.commit()

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

            # Add course to DB
            for course in courses_students:
                st_list = []
                for student in courses_students[course]:
                    fn, ln = student.split(' ')
                    st = Student.query.filter_by(
                        first_name=fn, last_name=ln).first()
                    st_list.append(st)
                db.session.add(Course(name=course, students=st_list))
            db.session.flush()
            db.session.commit()

            return 'Data added'

    @api.representation('application/json')
    def output_json(data, code, headers=None):
        resp = make_response(json.dumps(data, default=str), code)
        resp.headers.extend(headers or {})
        return resp

    class DropTables(Resource):
        def get(self):
            db.session.remove()
            db.drop_all()
            return 'Tables is reset'

    class FindGroups(Resource):
        def get(self, students):
            q = db.session.query(Group).join(Student).group_by(
                Group.id).having(func.count(Student.id) <= students)
            return group_schema.dump(q)

    class FindCourse(Resource):
        def get(self, course):
            q = db.session.query(
                schedule,
                Student.first_name,
                Student.last_name).join(
                Student,
                Course).filter(
                Course.name.like(
                    "%{}%".format(course)))
            return schedule_schema.dump(q)

    class WorkWithStudent(Resource):
        def post(self):
            data = request.get_json()
            first_n = request.form['first_n']
            last_n = request.form['last_n']
            st = Student(first_name=first_n, last_name=last_n)
            db.session.add(st)
            db.session.commit()
            return st.id

        def delete(self):
            stud_id = request.form['id']
            st = Student.query.filter(Student.id == stud_id).one()
            db.session.delete(st)
            db.session.commit()
            return st.id

    class WorkWithCourse(Resource):
        def post(self):
            course = request.form['course']
            first_n = request.form['first_n']
            last_n = request.form['last_n']
            st = Student.query.filter(
                Student.first_name.like(first_n),
                Student.last_name.like(last_n)).one()
            c = Course.query.filter(Course.name.like(course)).one()
            c.students.append(st)
            db.session.add(c)
            db.session.commit()
            return c.id

        def delete(self):
            course = request.form['course']
            first_n = request.form['first_n']
            last_n = request.form['last_n']
            st = Student.query.filter(
                Student.first_name.like(first_n),
                Student.last_name.like(last_n)).one()
            c = Course.query.filter(Course.name.like(course)).one()
            c.students.remove(st)
            db.session.add(c)
            db.session.commit()
            return c.id

    api.add_resource(CreateData, '/fill')
    api.add_resource(DropTables, '/drop')
    api.add_resource(FindGroups, '/groups/<int:students>')
    api.add_resource(FindCourse, '/course/<string:course>')
    api.add_resource(WorkWithStudent, '/student')
    api.add_resource(WorkWithCourse, '/course')
    return app


if __name__ == '__main__':
    app = create_app()
    app.app_context().push()
    db.create_all()
    app.run(debug=True)
