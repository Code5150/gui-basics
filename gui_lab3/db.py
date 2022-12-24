from peewee import *

DB_NAME = 'myDatabase.sqlite'


class DatabaseConnection(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.__db__ = SqliteDatabase(DB_NAME)
        return cls._instance

    def connect_db(self):
        return self._instance.__db__.connect(True)

    def connected(self):
        return self._instance.__db__.is_connection_usable()

    def get_db(self):
        return self._instance.__db__

    def close_db(self):
        result = True
        if not self._instance.__db__.is_closed():
            result = self._instance.__db__.close()
        return result
