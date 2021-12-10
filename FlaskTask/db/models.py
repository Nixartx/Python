from peewee import *

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
    start = DateTimeField()
    finish = DateTimeField()
    time = TimeField()
    driver_id = ForeignKeyField(Driver)

    class Meta:
        db_table = 'races'
