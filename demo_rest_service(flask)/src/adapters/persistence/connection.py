import os
from typing import Callable

from dotenv import load_dotenv
import pymysql

load_dotenv()

def get_database():
    return {
        "host": os.environ.get("DATABASE_HOST"),
        "port": int(os.environ.get("DATABASE_PORT")),
        "user": os.environ.get("DATABASE_USERNAME"),
        "password": os.environ.get("DATABASE_PASSWORD"),
        "database": os.environ.get("DATABASE_NAME"),
    }

class Connection:

    def __init__(self):
        self.connection = pymysql.connect(**get_database())

    def perform(self, call: Callable):
        try:
            with self.connection.cursor() as cursor:
                result = call(cursor)
            self.connection.commit()
            return result
        except Exception as exception:
            self.connection.rollback()
            print(exception)
        finally:
            self.connection.close()
