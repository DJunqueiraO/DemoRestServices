from typing import TypeVar, Generic, List, Optional, Type
from sqlalchemy.orm import Session

E = TypeVar("E")
M = TypeVar("M")

class Repository(Generic[E, M]):
    def __init__(self, session: Session, model_cls: Type[M], entity_cls: Type[E]):
        self._session = session
        self._model_cls = model_cls
        self._entity_cls = entity_cls

    def _to_entity(self, model) -> E:
        if not model:
            return None
        return self._entity_cls(id_=model.id, name=model.name)

    def find_all(self) -> List[E]:
        try:
            models = self._session.query(self._model_cls).all()
            return [self._to_entity(m) for m in models]
        finally:
            self._session.close()

    def find_by_id(self, id_: int) -> Optional[E]:
        try:
            model = self._session.query(self._model_cls).filter_by(id=id_).first()
            return self._to_entity(model)
        finally:
            self._session.close()

    def save(self, entity: E) -> E:
        try:
            model = self._model_cls(**entity)
            self._session.add(model)
            self._session.commit()
            self._session.refresh(model)
            entity["id"] = model.id
            return entity
        except Exception as e:
            self._session.rollback()
            raise e
        finally:
            self._session.close()

    def update(self, entity: E) -> Optional[E]:
        try:
            id_ = entity.get_id()
            model = self._session.query(self._model_cls).filter_by(id=id_).first()

            if not model:
                return None

            for key, value in entity.items():
                if key != "id" and hasattr(model, key):
                    setattr(model, key, value)

            self._session.commit()
            return entity
        except Exception as e:
            self._session.rollback()
            raise e
        finally:
            self._session.close()

    def delete_by_id(self, id_: int) -> bool:
        try:
            model = self._session.query(self._model_cls).filter_by(id=id_).first()
            if not model:
                return False

            self._session.delete(model)
            self._session.commit()
            return True
        except Exception as e:
            self._session.rollback()
            raise e
        finally:
            self._session.close()