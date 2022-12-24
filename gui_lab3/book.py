from peewee import *

from db import DatabaseConnection


class Book(Model):
    id = IntegerField()
    name = TextField()
    description = TextField()
    author = TextField()
    genre = TextField()
    price = IntegerField()

    def get_by_attr_name(self, attr_name):
        return self.__dict__['__data__'][attr_name]

    class Meta:
        database = DatabaseConnection().get_db()
        db_table = 'book'

