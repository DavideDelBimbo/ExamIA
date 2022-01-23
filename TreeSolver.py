import random
from typing import List, Optional

from Class.Assignment import Assignment
from Class.CSP import CSP
from Class.Constraint import Constraint
from Class.Variable import Variable


def __selectRoot(csp: CSP, visited: List[Variable]) -> Variable:
    unvisited: set[Variable] = csp.getVariables() - set(visited)
    return random.choice(list(unvisited))

def __topologicalSort(csp: CSP, ass: Assignment) -> List[List[Variable]]:
    def __topologicalSortUtil(csp: CSP, var: Variable, visited: List[Variable], sorting: List[Variable]) -> tuple[List[Variable], List[Variable]]:
        visited.append(var)
        sorting.append(var)

        children = []
        for neighbour in csp.getGraphConstraint()[var]:
            if not visited.__contains__(neighbour):
                children.append(neighbour)

        for child in children:
            __topologicalSortUtil(csp, child, visited, sorting)
        return visited, sorting

    visited: List[Variable] = []
    sortingList: List[List[Variable]] = []

    for varAssigned in ass.getAssignment():
        visited.append(varAssigned)

    while len(visited) < len(csp.getVariables()):
        root: Variable = __selectRoot(csp, visited)
        sorting: List[Variable] = []
        visited, sorting = __topologicalSortUtil(csp, root, visited, sorting)
        sortingList.append(sorting)

    return sortingList

def __makeArcConsistency(csp: CSP, sorting: List[Variable]) -> bool:
    def __revise(Xi: Variable, Xj: Variable, cons: Constraint) -> bool:
        revised = False

        for i in Xi.getVariableDomain().getLegalValues():
            for j in Xj.getVariableDomain().getLegalValues():
                if cons.checkConstraint(i, j):
                    break
            else:
                Xi.getVariableDomain().setIllegalValue(i)
                revised = True
        return revised

    for i in range(len(sorting) - 1, 0, -1):
        for j in range(i-1, 0, -1):
            #look if sequence[j] is parent of sequence[i] until the root
            if csp.getConstraintsForVar(sorting[j]).__contains__(sorting[i]):
                __revise(sorting[j], sorting[i], csp.getConstraint(sorting[j], sorting[i]))

        if sorting[i].getVariableDomain().getLegalValues() == 0:
            return False
    return True

def __isConsistent(csp: CSP, ass: Assignment, var: Variable) -> bool:
    assignment = ass.getAssignment()
    assignedValue = assignment[var]
    if not var.getVariableDomain().getLegalValues().__contains__(assignedValue):
        return False
    if csp.getGraphConstraint().__contains__(var):
        for var2 in assignment:
            if var2 != var:
                if csp.getGraphConstraint()[var].__contains__(var2):
                    if not csp.getConstraint(var, var2).checkConstraint(assignedValue, assignment[var2]):
                        return False
    return True

def treeSolver(csp: CSP, ass: Assignment) -> Optional[Assignment]:
    X: List[List[Variable]] = __topologicalSort(csp, ass)

    print('Topological sort:', end=' ')
    for sort in X:
        print('[', end='')
        for i in range(len(sort)):
            if i < len(sort) - 1:
                print(sort[i].getVariableName(), end=' ')
            else:
                print(sort[i].getVariableName(), end='')
        print(']', end='')
    print()

    for sort in X:
        if not __makeArcConsistency(csp, sort):
            return None
        for var in sort:
            for val in var.getVariableDomain().getLegalValues():
                ass.addAssignment(var, val)
                if __isConsistent(csp, ass, var):
                    break
                else:
                    ass.removeAssignment(var)
            else:
                return None
    return ass