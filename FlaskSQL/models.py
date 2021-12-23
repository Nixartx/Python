from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Group(db.Model):
    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    students = db.relationship(
        'Student', backref=db.backref(
            'students', lazy=True, uselist=True))


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    group_id = db.Column(
        db.Integer,
        db.ForeignKey('groups.id'),
        nullable=False)


class Course(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text)


class Schedule(db.Model):
    __tablename__ = "courses_groups"

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(
        db.Integer,
        db.ForeignKey('courses.id'),
        nullable=False)
    course = db.relationship(
        'Course', backref=db.backref(
            'courses', lazy=True))
    group_id = db.Column(
        db.Integer,
        db.ForeignKey('groups.id'),
        nullable=False)
    group = db.relationship('Group', backref=db.backref('groups', lazy=True))
