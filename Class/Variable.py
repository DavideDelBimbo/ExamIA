from copy import deepcopy

from Class.Domain import Domain


class Variable:
    def __init__(self, name: str, domain: Domain) -> None:
        self.__name: str = name
        self.__domain: Domain = deepcopy(domain)

    def getVariableName(self) -> str:
        return self.__name

    def getVariableDomain(self) -> Domain:
        return self.__domain
