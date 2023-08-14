from typing import TypeVar, Generic, Union

T = TypeVar("T")
U = TypeVar("U")


class Just(Generic[T]):
    __match_args__ = ("_val",)

    def __init__(self, val: T):
        self._val = val

    def unwrap(self):
        return self._val

    def __str__(self):
        return f"Some({self._val})" if self._val is not None else "Nothing"

    def __repr__(self):
        return f"Some({self._val})" if self._val is not None else "Nothing"


Nothing = Just[None]
Maybe = Nothing | Just[T]


class Left(Generic[T]):
    __match_args__ = ("_val",)

    def __init__(self, val):
        self._val = val


class Right(Generic[T]):
    __match_args__ = ("_val",)

    def __init__(self, val):
        self._val = val


Either = Left[T] | Right[U]
