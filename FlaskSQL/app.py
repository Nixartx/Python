from flask import Flask, make_response, abort, request
import os
import json
from FlaskSQL.models import *
from FlaskSQL.schema import *
from flask_restful import Resource, Api, reqparse
from sqlalchemy import func, exc


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


    class GroupsRes(Resource):
        def get(self):
            students = request.args.get('students_number', 0)
            q = db.session.query(Group).join(Student).group_by(
                Group.id).having(func.count(Student.id) <= students)
            return group_schema.dump(q)

    class CourseRes(Resource):
        def get(self):
            course = request.args.get('course_name', None)
            q = db.session.query(
                schedule,
                Student.first_name,
                Student.last_name).join(
                Student,
                Course).filter(
                Course.name == course)
            return schedule_schema.dump(q)

    class StudentRes(Resource):
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
            except exc.NoResultFound:
                abort(404)
            db.session.delete(st)
            db.session.commit()
            return None, 204

    class StudentCourses(Resource):
        def post(self, student_id):
            parser = reqparse.RequestParser()
            parser.add_argument('courses_list', action='append')
            args = parser.parse_args()
            try:
                st = Student.query.filter(
                    Student.id == student_id).one()
                for course_name in args['courses_list']:
                    c = Course.query.filter(Course.name == course_name).one()
                    c.students.append(st)
                    db.session.add(c)
            except exc.NoResultFound:
                abort(404)
            db.session.commit()
            return None, 201

    class StudentCourse(Resource):
        def delete(self, student_id, course_id):
            try:
                sc = schedule.delete().filter(
                    schedule.columns.student_id == student_id,
                    schedule.columns.course_id == course_id)
                db.session.execute(sc)
            except exc.NoResultFound:
                abort(404)
            db.session.commit()
            return None, 204

    api.add_resource(GroupsRes, '/groups')
    api.add_resource(CourseRes, '/course')
    api.add_resource(StudentRes, '/student/<string:student>')
    api.add_resource(
        StudentCourses,
        '/student/<int:student_id>/courses')
    api.add_resource(
        StudentCourse,
        '/student/<int:student_id>/course/<int:course_id>')
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
