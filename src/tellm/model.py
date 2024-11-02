""" Model interface used to unify the model implementations. """
from abc import ABC, abstractmethod

class Model(ABC):
    """ Abstract Base Class of all model implementations."""

    @property
    @abstractmethod
    def system_prompt(self):
        """The system prompt to use in the model."""

    @system_prompt.setter
    @abstractmethod
    def system_prompt(self, value: str):
        pass
