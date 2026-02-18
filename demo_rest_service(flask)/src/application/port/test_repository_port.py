from abc import ABC

from src.application.port.repository_port import RepositoryPort
from src.domain.entity.test import Test


class TestRepositoryPort(RepositoryPort[Test], ABC):
    def __init__(self):
        super().__init__(Test)