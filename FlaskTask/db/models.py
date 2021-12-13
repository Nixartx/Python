from peewee import *
from playhouse.hybrid import hybrid_property
import datetime

db = SqliteDatabase('db/monaco.db')


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
        return self.start - self.finish
        #return self.start
        # return datetime.datetime(self.finish.)-datetime.datetime(self.start)

    # @time.expression
    # def time(cls):
    #     return fn.JULIANDAY(cls.finish)-fn.JULIANDAY(cls.start)

    class Meta:
        db_table = 'races'
