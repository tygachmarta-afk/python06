import abc


class TransformCapability(abc.ABC):
    def __init__(self) -> None:
        self.transformed: bool = False

    @abc.abstractmethod
    def transform(self) -> str:
        pass

    @abc.abstractmethod
    def revert(self) -> str:
        pass