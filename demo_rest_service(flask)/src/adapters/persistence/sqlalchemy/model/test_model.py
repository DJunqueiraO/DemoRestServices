from sqlalchemy import Column, Integer, String

from src.adapters.persistence.sqlalchemy.model.model import Model


class TestModel(Model):
    __tablename__ = "test"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)

    def get_name(self):
        return self.__tablename__