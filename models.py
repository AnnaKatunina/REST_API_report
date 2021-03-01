from peewee import *

db = SqliteDatabase('drivers.db')


class Driver(Model):
    driver_id = CharField(unique=True)
    name = CharField()
    team = CharField()
    result = TimeField()

    class Meta:
        database = db


Driver.create_table()
