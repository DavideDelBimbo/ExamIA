from __future__ import annotations
from typing import Set, Dict, Optional

from Class.Assignment import Assignment
from Class.Constraint import Constraint
from Class.Variable import Variable


class CSP:
    def __init__(self) -> None:
        self.__variables: Set[Variable] = set()
        self.__graphConstraints: Dict[Variable, Dict[Variable, Constraint]] = {}

    def __copy__(self, ass: Assignment) -> CSP:
        new = CSP()
        for vertex in self.__variables:
            if not ass.getAssignment().__contains__(vertex):
                new.addVariable(vertex)
        for edge in self.getEdges():
            if not ass.getAssignment().__contains__(edge[0]) and not ass.getAssignment().__contains__(edge[1]):
                new.addConstraint(edge[0], edge[1], self.getConstraint(edge[0], edge[1]))
        return new

    def addVariable(self, var: Variable) -> None:
        self.__variables.add(var)
        self.__graphConstraints[var] = {}

    def getVariables(self) -> Set[Variable]:
        return self.__variables.copy()

    def getVariablesSize(self) -> int:
        return len(self.__variables)

    def addConstraint(self, var1: Variable, var2: Variable, cons: Constraint) -> None:
        if self.__variables.__contains__(var1) and self.__variables.__contains__(var2):
            self.__graphConstraints[var1][var2] = cons
            self.__graphConstraints[var2][var1] = cons

    def getGraphConstraint(self) -> Dict[Variable, Dict[Variable, Constraint]]:
        return self.__graphConstraints.copy()

    def getConstraint(self, var1: Variable, var2: Variable) -> Optional[Constraint]:
        if self.__graphConstraints.__contains__(var1) and self.__graphConstraints[var1].__contains__(var2):
            return self.__graphConstraints[var1][var2]
        else:
            return None

    def getConstraintsForVar(self, var: Variable) -> Dict[Variable, Constraint]:
        if self.__variables.__contains__(var):
            return self.__graphConstraints[var]
        else:
            return {}

    def getEdges(self) -> Set[tuple[Variable, Variable]]:
        edges: Set[tuple[Variable, Variable]] = set()
        for var1 in self.__graphConstraints:
            for var2 in self.__graphConstraints[var1]:
                edges.add((var1, var2))
        return edges

    def getNeighbour(self, var: Variable) -> Set[tuple[Variable, Variable]]:
        neighbour: Set[tuple[Variable, Variable]] = set()
        if self.__graphConstraints.__contains__(var):
            for var2 in self.__graphConstraints[var]:
                neighbour.add((var, var2))
                neighbour.add((var2, var))
        return neighbour