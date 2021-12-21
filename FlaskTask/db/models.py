from peewee import *
from playhouse.hybrid import hybrid_property
import os

db = SqliteDatabase(os.path.join(os.path.dirname(__file__), 'monaco.db'))


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'


class Driver(BaseModel):
    short_name = CharField(max_length=3)
    full_name = TextField()
    car = TextField()

    class Meta:
        db_table = 'drivers'


class Race(BaseModel):
    start = DateTimeField(null=True)
    finish = DateTimeField(null=True)
    driver = ForeignKeyField(Driver)

    @hybrid_property
    def time(self):
        return self.finish - self.start

    @time.expression
    def time(cls):
        return fn.STRFTIME(
            '%H:%M:%f',
            fn.JULIANDAY(
                cls.finish) -
            fn.JULIANDAY(
                cls.start),
            '12 hours')

    class Meta:
        db_table = 'races'
