from flask import Flask, make_response, request, abort
import os
import json
from FlaskSQL.models import *
from FlaskSQL.schema import *
from flask_restful import Resource, Api
from FlaskSQL.generate import *
from sqlalchemy import func


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object('FlaskSQL.config.Config')
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    db.init_app(app)
    api = Api(app)

    # Marshmallow schema
    group_schema = GroupSchema(many=True)
    schedule_schema = ScheduleSchema(many=True)
    student_schema = StudentSchema()

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @api.representation('application/json')
    def output_json(data, code, headers=None):
        resp = make_response(json.dumps(data, default=str), code)
        resp.headers.extend(headers or {})
        return resp

    class FindGroups(Resource):
        def get(self, students):
            q = db.session.query(Group).join(Student).group_by(
                Group.id).having(func.count(Student.id) <= students)
            return group_schema.dump(q)

    class FindCourses(Resource):
        def get(self, course):
            q = db.session.query(
                schedule,
                Student.first_name,
                Student.last_name).join(
                Student,
                Course).filter(
                Course.name == course)
            return schedule_schema.dump(q)

    class WorkWithStudents(Resource):
        def post(self, student):
            first_n, last_n = student.split(' ')
            st = Student(first_name=first_n, last_name=last_n)
            db.session.add(st)
            db.session.commit()
            return student_schema.dump(st), 201

        def delete(self, student):
            stud_id = student
            try:
                st = Student.query.filter(Student.id == stud_id).one()
            except BaseException:
                abort(403)
            db.session.delete(st)
            db.session.commit()
            return {}, 204

    class WorkWithCourses(Resource):
        def post(self, student_id, course_id):
            try:
                st = Student.query.filter(
                    Student.id == student_id).one()
                c = Course.query.filter(Course.id == course_id).one()
            except BaseException:
                abort(403)
            c.students.append(st)
            db.session.add(c)
            db.session.commit()
            return {}, 201

        def delete(self, student_id, course_id):
            try:
                st = Student.query.filter(
                    Student.id == student_id).one()
                c = Course.query.filter(Course.id == course_id).one()
                sc = schedule.query.filter(schedule.student_id == student_id, schedule.course_id == course_id)
            except BaseException:
                abort(403)
            c.students.remove(st)
            db.session.add(c)
            db.session.commit()
            return {}, 204

    api.add_resource(FindGroups, '/groups/<int:students>')
    api.add_resource(FindCourses, '/course/<string:course>')
    api.add_resource(WorkWithStudents, '/student/<string:student>')
    api.add_resource(
        WorkWithCourses,
        '/students/<int:student_id>/courses/<int:course_id>')
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
