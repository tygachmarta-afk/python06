import abc

from ex3.creature import Creature


class BattleStrategy(abc.ABC):
    def __init__(self, label: str) -> None:
        self.label = label

    @abc.abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abc.abstractmethod
    def act(self, creature: Creature) -> None:
        pass