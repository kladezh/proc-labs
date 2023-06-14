from __future__ import annotations
from enum import Enum
import math


class BinaryOperation(Enum):
    Substract = (1, "-", lambda x, y: x - y)
    Add = (2, "+", lambda x, y: x + y)
    Divide = (3, "/", lambda x, y: x // y)
    Mulptiply = (4, "*", lambda x, y: x * y)
    Power = (5, "^", lambda x, y: x**y)

    def __init__(self, priority: int, string: str, action: function) -> None:
        self.priority = priority
        self.string = string
        self.action = action

    @classmethod
    def fromstr(cls, string: str) -> BinaryOperation | None:
        for op in cls:
            if op.string == string:
                return op
        return None

    @classmethod
    def isstr(cls, string: str) -> bool:
        for op in cls:
            if op.string == string:
                return True
        return False


class PostfixFunction(Enum):
    Factorial = ("!", lambda x: math.factorial(x))

    def __init__(self, string: str, action: function) -> None:
        self.string = string
        self.action = action

    @classmethod
    def fromstr(cls, string: str) -> PostfixFunction | None:
        for op in cls:
            if op.string == string:
                return op
        return None

    @classmethod
    def isstr(cls, string: str) -> bool:
        for op in cls:
            if op.string == string:
                return True
        return False


class PrefixFunction(Enum):
    Sin = ("sin", lambda x: math.sin(x))
    Cos = ("cos", lambda x: math.cos(x))
    Tan = ("tan", lambda x: math.tan(x))
    Log = ("log", lambda x: math.log(x))
    Sqrt = ("sqrt", lambda x: math.sqrt(x))

    def __init__(self, string: str, action: function) -> None:
        self.string = string
        self.action = action

    @classmethod
    def fromstr(cls, string: str) -> PrefixFunction | None:
        for op in cls:
            if op.string == string:
                return op
        return None

    @classmethod
    def isstr(cls, string: str) -> bool:
        for op in cls:
            if op.string == string:
                return True
        return False
