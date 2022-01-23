from typing import Iterable, Set, Any


class Domain:
    def __init__(self, values: Iterable) -> None:
        self.__values: Set[Any] = set(values)
        self.__illegal: Set[Any] = set()

    def getLegalValues(self) -> Set:
        return self.__values - self.__illegal

    def getLegalSize(self) -> int:
        return len(self.__values - self.__illegal)

    def checkValue(self, val: Any) -> bool:
        if self.__values.__contains__(val):
            return True
        return False

    def setIllegalValue(self, val: Any) -> None:
        if self.__values.__contains__(val):
            self.__illegal.add(val)