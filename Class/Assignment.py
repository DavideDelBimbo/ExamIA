from typing import Dict, Any, Set

from Class.Variable import Variable


class Assignment:
    def __init__(self) -> None:
        self.__assignment: Dict[Variable, Any] = {}
        self.__inferences: Dict[Variable, Set[Any]] = {}

    def __copy__(self):
        new = Assignment()
        for var in self.__assignment:
            new.addAssignment(var, self.__assignment[var])
        for var in self.__inferences:
            for value in self.__inferences[var]:
                new.addInference(var, value)
        return new

    def addAssignment(self, var: Variable, val:  Any) -> None:
        if var.getVariableDomain().checkValue(val):
            self.__assignment[var] = val

    def removeAssignment(self, var: Variable):
        self.__assignment.pop(var)

    def getAssignment(self) -> Dict[Variable, Any]:
        return self.__assignment.copy()

    def addInference(self, var: Variable, val: Any) -> None:
        if var.getVariableDomain().checkValue(val):
            if not self.__inferences.__contains__(var):
                self.__inferences[var] = set()
            self.__inferences[var].add(val)

    def deleteInference(self, var: Variable, val: Any) -> None:
        if self.__inferences.__contains__(var):
            self.__inferences.pop(val)

    def getInferences(self) -> Dict[Variable, Set[Any]]:
        return self.__inferences.copy()

    def getInferencesForVar(self, var: Variable) -> Set[Any]:
        if self.__inferences.__contains__(var):
            return self.__inferences[var].copy()
        else:
            return set()