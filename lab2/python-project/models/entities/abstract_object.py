from abc import ABC, abstractmethod


class AObject(ABC):
    @abstractmethod
    def to_string(self):
        pass

    @staticmethod
    @abstractmethod
    def input_from_console():
        pass
