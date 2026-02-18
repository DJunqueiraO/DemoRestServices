from abc import ABC
from typing import Optional

from sqlalchemy.orm import Session

from src.adapters.persistence.sqlalchemy.model.demo_model import DemoModel
from src.application.port.demo_repository_port import DemoRepositoryPort
from src.domain.entity.demo import Demo


class DemoRepository(DemoRepositoryPort, ABC):

    def __init__(self, session: Session):
        self._session = session

    def find_all(self) -> list[Demo]:
        demos = self._session.query(DemoModel).all()
        self._session.close()

        result = [Demo(id_=d.id, name=d.name) for d in demos]
        return result

    def find_by_id(self, id_: int) -> Optional[Demo]:
        demo = self._session.query(DemoModel).filter_by(id=id_).first()
        self._session.close()

        if not demo:
            return None

        return Demo(id_=demo.id, name=demo.name)

    def save(self, demo: Demo) -> Demo:
        model = DemoModel(**demo)
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        self._session.close()
        demo["id"] = model.id
        return demo

    def update(self, demo: Demo) -> Demo:
        model = self._session.query(DemoModel).filter_by(id=demo.get_id()).first()

        if not model:
            self._session.close()
            raise ValueError(f"Demo com id {demo.get_id()} não encontrado.")

        for key, value in demo.items():
            if key != "id" and hasattr(model, key):
                setattr(model, key, value)

        try:
            self._session.commit()
        except Exception as e:
            self._session.rollback()
            raise e
        finally:
            self._session.close()

        return demo

    def delete_by_id(self, id_: int) -> bool:
        demo = self._session.query(DemoModel).filter_by(id=id_).first()

        if not demo:
            self._session.close()
            return False

        self._session.delete(demo)
        self._session.commit()
        self._session.close()

        return True