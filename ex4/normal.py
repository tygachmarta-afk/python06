from ex3.creature import Creature

from .base import BattleStrategy
from .errors import InvalidStrategyError


class NormalStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__("normal")

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(creature.name, self.label)
        print(creature.attack())