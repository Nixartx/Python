from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Group(db.Model):
    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    students = db.relationship(
        'Student', backref=db.backref(
            'students',))


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    group_id = db.Column(
        db.Integer,
        db.ForeignKey('groups.id'),
        nullable=False)

schedule = db.Table('schedule',
                db.Column('course_id', db.Integer, db.ForeignKey('courses.id'), primary_key=True),
                db.Column('group_id', db.Integer, db.ForeignKey('groups.id'), primary_key=True)
                )

class Course(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text)
    groups=db.relationship(
        'Group', secondary=schedule, backref=db.backref(
            'groups'))






