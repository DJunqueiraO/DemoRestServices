from abc import ABC
from typing import Optional

from sqlalchemy.orm import Session

from src.adapters.persistence.sqlalchemy.model.test_model import TestModel
from src.application.port.test_repository_port import TestRepositoryPort
from src.domain.entity.test import Test


class TestRepository(TestRepositoryPort, ABC):

    def __init__(self, session: Session):
        self._session = session

    def find_all(self) -> list[Test]:
        tests = self._session.query(TestModel).all()
        self._session.close()

        result = [Test(id_=d.id, name=d.name) for d in tests]
        return result

    def find_by_id(self, id_: int) -> Optional[Test]:
        test = self._session.query(TestModel).filter_by(id=id_).first()
        self._session.close()

        if not test:
            return None

        return Test(id_=test.id, name=test.name)

    def save(self, test: Test) -> Test:
        model = TestModel(**test)
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        self._session.close()
        test["id"] = model.id
        return test

    def update(self, test: Test) -> Test:
        model = self._session.query(TestModel).filter_by(id=test.get_id()).first()

        if not model:
            self._session.close()
            raise ValueError(f"Test com id {test.get_id()} não encontrado.")

        for key, value in test.items():
            if key != "id" and hasattr(model, key):
                setattr(model, key, value)

        try:
            self._session.commit()
        except Exception as e:
            self._session.rollback()
            raise e
        finally:
            self._session.close()

        return test

    def delete_by_id(self, id_: int) -> bool:
        test = self._session.query(TestModel).filter_by(id=id_).first()

        if not test:
            self._session.close()
            return False

        self._session.delete(test)
        self._session.commit()
        self._session.close()

        return True