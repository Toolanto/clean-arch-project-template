from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from pydantic import BaseModel

E = TypeVar("E", bound=BaseModel)


class BaseUseCase(ABC, Generic[E]):
    @abstractmethod
    def execute(self, *args, **kwargs) -> E | None:
        """
        Execute a use case and return an generic type

        Returns: E an entity
        """

