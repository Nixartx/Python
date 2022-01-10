from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.functions import func

db = SQLAlchemy()


class Group(db.Model):
    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    #students = db.relationship('Student', backref=db.backref('students'))


schedule = db.Table(
    'schedule',
    db.Column(
        'course_id',
        db.Integer,
        db.ForeignKey('courses.id')),
    db.Column(
        'student_id',
        db.Integer,
        db.ForeignKey('students.id')))


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    group_id = db.Column(
        db.Integer,
        db.ForeignKey('groups.id'),
        nullable=True)


class Course(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text)
    students = db.relationship(
        'Student', secondary=schedule, backref=db.backref(
            'students'))
