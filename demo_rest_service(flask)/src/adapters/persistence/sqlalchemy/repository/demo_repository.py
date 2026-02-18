from src.adapters.persistence.sqlalchemy.model.demo_model import DemoModel
from src.application.port.demo_repository_port import DemoRepositoryPort
from src.domain.entity.demo import Demo
from src.adapters.persistence.sqlalchemy.repository.repository import Repository
from sqlalchemy.orm import Session

class DemoRepository(Repository[Demo, DemoModel], DemoRepositoryPort):
    def __init__(self, session: Session):
        super().__init__(session, DemoModel, Demo)