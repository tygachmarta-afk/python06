from ex3.capability import TransformCapability
from ex3.creature import Creature

from .base import BattleStrategy
from .errors import InvalidStrategyError


class AggressiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__("aggressive")

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, TransformCapability):
            raise InvalidStrategyError(creature.name, self.label)
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())