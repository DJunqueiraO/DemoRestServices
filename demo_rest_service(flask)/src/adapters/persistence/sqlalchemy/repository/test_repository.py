from src.adapters.persistence.sqlalchemy.model.test_model import TestModel
from src.application.port.test_repository_port import TestRepositoryPort
from src.domain.entity.test import Test
from src.adapters.persistence.sqlalchemy.repository.repository import Repository
from sqlalchemy.orm import Session

class TestRepository(Repository[Test, TestModel], TestRepositoryPort):
    def __init__(self, session: Session):
        super().__init__(session, TestModel, Test)