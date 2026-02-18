from abc import ABC

from src.application.port.repository_port import RepositoryPort
from src.domain.entity.demo import Demo


class DemoRepositoryPort(RepositoryPort[Demo], ABC):
    def __init__(self):
        super().__init__()