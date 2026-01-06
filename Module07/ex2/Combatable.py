from abc import ABC, abstractmethod


class Combatable(ABC):
    @abstractmethod
    def attack(self, target) -> dict:
        pass
