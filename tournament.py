from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory
from ex4 import (
    AggressiveStrategy,
    BattleStrategy,
    InvalidStrategyError,
    NormalStrategy,
)

Opponent = tuple[CreatureFactory, BattleStrategy]


def battle(opponents: list[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                factory_one, strategy_one = opponents[i]
                factory_two, strategy_two = opponents[j]
                fighter_one = factory_one.create_base()
                fighter_two = factory_two.create_base()
                print("* Battle *")
                print(fighter_one.describe())
                print(" vs.")
                print(fighter_two.describe())
                print(" now fight!")
                strategy_one.act(fighter_one)
                strategy_two.act(fighter_two)
    except InvalidStrategyError as error:
        print(f"Battle error, aborting tournament: {error}")


def describe_opponents(opponents: list[Opponent]) -> str:
    parts = ", ".join(
        f"({factory.create_base().name}+{strategy.label.capitalize()})"
        for factory, strategy in opponents
    )
    return f"[ {parts} ]"


if __name__ == "__main__":
    flame_factory = FlameFactory()
    transform_factory = TransformCreatureFactory()
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()

    tournaments: list[tuple[str, list[Opponent]]] = [
        ("basic", [(flame_factory, normal), (transform_factory, aggressive)]),
        ("error", [(transform_factory, aggressive),
                   (flame_factory, aggressive)]),
    ]

    for index, (title, opponents) in enumerate(tournaments):
        if index > 0:
            print()
        print(f"Tournament {index} ({title}) {describe_opponents(opponents)}")
        battle(opponents)