class InvalidStrategyError(Exception):
    def __init__(self, creature_name: str, strategy_label: str) -> None:
        super().__init__(
            f"Invalid Creature '{creature_name}' "
            f"for this {strategy_label} strategy"
        )