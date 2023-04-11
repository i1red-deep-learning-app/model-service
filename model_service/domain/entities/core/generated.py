from typing import TypeVar, Annotated, TypeGuard, Any, get_origin, get_args, Final

T = TypeVar("T")
Generated = Annotated[T, "Generated"]


class GeneratedType:
    def __repr__(self) -> str:
        return "GENERATED_VALUE"


GENERATED_VALUE: Final = GeneratedType()


def is_generated(t: type) -> TypeGuard[Generated[Any]]:
    if get_origin(t) != Annotated:
        return False

    match get_args(t):
        case _, "Generated":
            return True
        case _:
            return False
