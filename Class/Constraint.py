from typing import Any


class Constraint:
    def __init__(self, function, name: str) -> None:
        self.__function = function
        self.__name: str = name

    def getConstraintFunction(self):
        return self.__function

    def getConstraintName(self) -> str:
        return self.__name

    def checkConstraint(self, val1: Any, val2: Any) -> bool:
        if self.__function(val1, val2):
            return True
        return False