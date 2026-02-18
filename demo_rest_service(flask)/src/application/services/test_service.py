from src.application.port.test_repository_port import TestRepositoryPort
from src.application.services.service import Service
from src.domain.entity.test import Test


class TestService(Service[Test, TestRepositoryPort]):
    def __init__(self, repository: TestRepositoryPort):
        super().__init__(repository)