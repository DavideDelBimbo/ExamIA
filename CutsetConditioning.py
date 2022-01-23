import random
from typing import List, Set, Optional, Any, Dict

from Class.Assignment import Assignment
from Class.CSP import CSP
from Class.Constraint import Constraint
from Class.Variable import Variable
from TreeSolver import treeSolver


def __getUnassignedVariable(csp: CSP, ass: Assignment) -> Variable:
    unassigned: set[Variable] = csp.getVariables() - ass.getAssignment().keys()

    min = [[list(unassigned)[0], len(csp.getGraphConstraint()[list(unassigned)[0]])]]

    for i in range(1, len(unassigned)):
        var = [list(unassigned)[i], len(csp.getGraphConstraint()[list(unassigned)[i]])]

        if var[0].getVariableDomain().getLegalSize() - len(ass.getInferencesForVar(var[0])) < min[0][
            0].getVariableDomain().getLegalSize() - len(ass.getInferencesForVar(min[0][0])):
            min = [var]
        else:
            if var[0].getVariableDomain().getLegalSize() - len(ass.getInferencesForVar(var[0])) == min[0][0].getVariableDomain().getLegalSize() - len(ass.getInferencesForVar(min[0][0])):
                if var[1] > min[0][1]:
                    min = [var]
                else:
                    if var[1] == min[0][1]:
                        min.append(var)
    return random.choice(min)[0]

def __getLegalValuesForVariable(ass: Assignment, var: Variable) -> List[Any]:
    return list(var.getVariableDomain().getLegalValues() - ass.getInferencesForVar(var))

def __maintainingArcConsistency(csp: CSP, ass: Assignment, queue : Set[tuple[Variable, Variable]]) -> bool:
    def __revise(Xi: Variable, Xj: Variable, cons: Constraint, ass: Assignment) -> bool:
        revised = False

        inferences = ass.getInferences()
        assignment = ass.getAssignment()
        if assignment.__contains__(Xi):
            valuesXi = {assignment[Xi]}
        else:
            valuesXi = Xi.getVariableDomain().getLegalValues()
            if inferences.__contains__(Xi):
                valuesXi -= inferences[Xi]
        if assignment.__contains__(Xj):
            valuesXj = {assignment[Xj]}
        else:
            valuesXj = Xj.getVariableDomain().getLegalValues()
            if inferences.__contains__(Xj):
                valuesXj -= inferences[Xj]

        for i in valuesXi:
            for j in valuesXj:
                if cons.checkConstraint(i, j):
                    break
            else:
                ass.addInference(Xi, i)
                revised = True
        return revised

    while len(queue) != 0:
        (Xi, Xj) = queue.pop()
        cons = csp.getConstraint(Xi, Xj)
        if ass.getAssignment().keys().__contains__(Xi) or ass.getAssignment().__contains__(Xj):
            if __revise(Xi, Xj, cons, ass):
                if Xi.getVariableDomain().getLegalSize() - len(ass.getInferencesForVar(Xi)) == 0:
                    return False

                for neighbor in csp.getConstraintsForVar(Xi):
                    if neighbor is not Xj:
                        queue.add((neighbor, Xi))
    return True

def __checkCycle(csp: CSP, ass: Assignment) -> bool:
    def __dfs(csp: CSP, var: Variable, visited: Dict[Variable, bool], parent) -> bool:
        visited[var] = True
        for child in csp.getGraphConstraint()[var]:
            if not visited[child]:
                if __dfs(csp, child, visited, var):
                    return True
            elif parent != child:
                return True
        return False

    visited = {}
    new = csp.__copy__(ass)

    for vertex in new.getVariables():
        visited[vertex] = False

    for vertex in new.getVariables():
        if not visited[vertex]:
            if __dfs(new, vertex, visited, -1):
                return True
    return False

def __backtrack(csp: CSP, ass: Assignment) -> Optional[Assignment]:
    if len(ass.getAssignment()) == csp.getVariablesSize():
        return ass

    if __checkCycle(csp, ass):
        #find cutset-cycle and do backtrack
        var: Variable = __getUnassignedVariable(csp, ass)
        values: List[Any] = __getLegalValuesForVariable(ass, var)

        for value in values:
            tryAssignment = ass.__copy__()
            tryAssignment.addAssignment(var, value)
            if __maintainingArcConsistency(csp, tryAssignment, csp.getNeighbour(var)):
                result = __backtrack(csp, tryAssignment)
                if result is not None:
                    return result
        return None
    else:
        #a tree was found
        if ass is not None:
            print('Cutset:', end=' ')
            for var in ass.getAssignment():
                print(var.getVariableName(), end=' ')
            print()

            result = treeSolver(csp, ass)
            return result
        return None

def cutsetConditioning(csp:CSP) -> Optional[Assignment]:
    assignment: Assignment = Assignment()
    return __backtrack(csp, assignment)