class DependencyKind:
    def __init__(self, type_name: str) -> None:
        self._type_name = type_name

    @property
    def type_name(self) -> str:
        return self._type_name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.type_name})"

    def __hash__(self) -> int:
        return hash(repr(self))


SINGLETON = DependencyKind("SINGLETON")
SCOPED = DependencyKind("SCOPED")
