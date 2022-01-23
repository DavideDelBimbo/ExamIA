from Class.CSP import CSP
from Class.Constraint import Constraint
from Class.Domain import Domain
from Class.Variable import Variable
from CutsetConditioning import cutsetConditioning


def printGrid(values):
    for i in range(len(values)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(values[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(values[i][j])
            else:
                print(str(values[i][j]) + " ", end="")

if __name__ == "__main__":
    print('MAP COLORING AUSTRALIA')
    australia = CSP()
    domainAustralia = Domain(['red', 'green', 'blue'])
    different = Constraint(lambda a, b: a != b, '≠')

    WA = Variable('Western Australia', domainAustralia)
    NT = Variable('Northern Territory', domainAustralia)
    Q = Variable('Queensland', domainAustralia)
    NSW = Variable('New South Wales', domainAustralia)
    V = Variable('Victoria', domainAustralia)
    SA = Variable('South Australia', domainAustralia)
    T = Variable('Tasmania', domainAustralia)

    print('Instanziate states as variables...')
    australia.addVariable(WA)
    australia.addVariable(NT)
    australia.addVariable(Q)
    australia.addVariable(NSW)
    australia.addVariable(V)
    australia.addVariable(SA)
    australia.addVariable(T)

    print('Instanziate costraints...')
    australia.addConstraint(WA, NT, different)
    australia.addConstraint(WA, SA, different)
    australia.addConstraint(SA, NT, different)
    australia.addConstraint(Q, NT, different)
    australia.addConstraint(Q, SA, different)
    australia.addConstraint(Q, NSW, different)
    australia.addConstraint(SA, NSW, different)
    australia.addConstraint(SA, V, different)
    australia.addConstraint(NSW, V, different)

    print('find a solution...')
    result = cutsetConditioning(australia)

    if result is not None:
        i = 0
        print('Result:', end=' ')
        for var in result.getAssignment():
            i += 1
            if i < len(result.getAssignment()):
                print(var.getVariableName() + ' -> ' + str(result.getAssignment()[var]), end=', ')
            else:
                print(var.getVariableName() + ' -> ' + str(result.getAssignment()[var]))
    else:
        print('UNSATISFACTABLE PROBLEM')
    print('-----------------------------------')

    print('MAP COLORING TUSCANY 1')
    tuscany = CSP()
    domainTuscany = Domain(['red', 'green', 'blue'])
    different = Constraint(lambda a, b: a != b, '≠')

    MS = Variable('Massa and Carrara', domainTuscany)
    LU = Variable('Lucca', domainTuscany)
    PI = Variable('Pisa', domainTuscany)
    LI = Variable('Livorno', domainTuscany)
    PT = Variable('Pistoia', domainTuscany)
    PO = Variable('Prato', domainTuscany)
    FI = Variable('Florence', domainTuscany)
    AR = Variable('Arezzo', domainTuscany)
    SI = Variable('Siena', domainTuscany)
    GR = Variable('Grosseto', domainTuscany)

    print('Instanziate region as variables...')
    tuscany.addVariable(MS)
    tuscany.addVariable(LU)
    tuscany.addVariable(PI)
    tuscany.addVariable(LI)
    tuscany.addVariable(PT)
    tuscany.addVariable(PO)
    tuscany.addVariable(FI)
    tuscany.addVariable(AR)
    tuscany.addVariable(SI)
    tuscany.addVariable(GR)

    print('Instanziate costraints...')
    tuscany.addConstraint(MS, LU, different)
    tuscany.addConstraint(PT, LU, different)
    tuscany.addConstraint(PI, LU, different)
    tuscany.addConstraint(FI, LU, different)
    tuscany.addConstraint(PT, PO, different)
    tuscany.addConstraint(PT, FI, different)
    tuscany.addConstraint(PO, FI, different)
    tuscany.addConstraint(FI, PI, different)
    tuscany.addConstraint(FI, SI, different)
    tuscany.addConstraint(FI, AR, different)
    tuscany.addConstraint(PI, SI, different)
    tuscany.addConstraint(PI, LI, different)
    tuscany.addConstraint(SI, AR, different)
    tuscany.addConstraint(PI, GR, different)
    tuscany.addConstraint(GR, LI, different)
    tuscany.addConstraint(GR, SI, different)

    print('find a solution...')
    result = cutsetConditioning(tuscany)

    if result is not None:
        i = 0
        print('Result:', end=' ')
        for var in result.getAssignment():
            i += 1
            if i < len(result.getAssignment()):
                print(var.getVariableName() + ' -> ' + str(result.getAssignment()[var]), end=', ')
            else:
                print(var.getVariableName() + ' -> ' + str(result.getAssignment()[var]))
    else:
        print('UNSATISFACTABLE PROBLEM')
    print('-----------------------------------')

    print('MAP COLORING TUSCANY 2')
    tuscany = CSP()
    domainTuscany = Domain(['red', 'green'])
    different = Constraint(lambda a, b: a != b, '≠')

    MS = Variable('Massa and Carrara', domainTuscany)
    LU = Variable('Lucca', domainTuscany)
    PI = Variable('Pisa', domainTuscany)
    LI = Variable('Livorno', domainTuscany)
    PT = Variable('Pistoia', domainTuscany)
    PO = Variable('Prato', domainTuscany)
    FI = Variable('Florence', domainTuscany)
    AR = Variable('Arezzo', domainTuscany)
    SI = Variable('Siena', domainTuscany)
    GR = Variable('Grosseto', domainTuscany)

    print('Instanziate region as variables...')
    tuscany.addVariable(MS)
    tuscany.addVariable(LU)
    tuscany.addVariable(PI)
    tuscany.addVariable(LI)
    tuscany.addVariable(PT)
    tuscany.addVariable(PO)
    tuscany.addVariable(FI)
    tuscany.addVariable(AR)
    tuscany.addVariable(SI)
    tuscany.addVariable(GR)

    print('Instanziate costraints...')
    tuscany.addConstraint(MS, LU, different)
    tuscany.addConstraint(PT, LU, different)
    tuscany.addConstraint(PI, LU, different)
    tuscany.addConstraint(FI, LU, different)
    tuscany.addConstraint(PT, PO, different)
    tuscany.addConstraint(PT, FI, different)
    tuscany.addConstraint(PO, FI, different)
    tuscany.addConstraint(FI, PI, different)
    tuscany.addConstraint(FI, SI, different)
    tuscany.addConstraint(FI, AR, different)
    tuscany.addConstraint(PI, SI, different)
    tuscany.addConstraint(PI, LI, different)
    tuscany.addConstraint(SI, AR, different)
    tuscany.addConstraint(PI, GR, different)
    tuscany.addConstraint(GR, LI, different)
    tuscany.addConstraint(GR, SI, different)

    print('find a solution...')
    result = cutsetConditioning(tuscany)

    if result is not None:
        i = 0
        print('Result:', end=' ')
        for var in result.getAssignment():
            i += 1
            if i < len(result.getAssignment()):
                print(var.getVariableName() + ' -> ' + str(result.getAssignment()[var]), end=', ')
            else:
                print(var.getVariableName() + ' -> ' + str(result.getAssignment()[var]))
    else:
        print('UNSATISFACTABLE PROBLEM')
    print('-----------------------------------')

    print('SUDOKU 1')
    sudoku = CSP()
    domainSudoku = Domain([1, 2, 3, 4, 5, 6, 7, 8, 9])
    different = Constraint(lambda a, b: a != b, '≠')

    row = 9
    column = 9
    cell = 3
    grid = {}
    values = [
        [0, 6, 0, 0, 0, 0, 7, 5, 0],
        [0, 0, 0, 0, 3, 6, 8, 0, 0],
        [0, 0, 2, 8, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 5],
        [9, 0, 8, 0, 0, 0, 1, 0, 7],
        [3, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 4, 2, 0, 0],
        [0, 0, 3, 6, 1, 0, 0, 0, 0],
        [0, 7, 9, 0, 0, 0, 0, 8, 0]
    ]
    printGrid(values)

    for i in range(1, row + 1):
        for j in range(1, column + 1):
            if values[i - 1][j - 1] != 0:
                grid["X{0}{1}".format(i, j)] = Variable('X' + str(i) + str(j), Domain([values[i - 1][j - 1]]))
            else:
                grid["X{0}{1}".format(i, j)] = Variable('X' + str(i) + str(j), domainSudoku)

    print('Instanziate region as variables...')
    for i in range(1, row + 1):
        for j in range(1, row + 1):
            sudoku.addVariable(grid['X' + str(i) + str(j)])

    print('Instanziate costraints...')
    for i in range(1, row + 1):
        for j in range(1, column + 1):
            for k in range(1, column + 1):
                if grid['X' + str(i) + str(j)] != grid['X' + str(i) + str(k)]:
                    sudoku.addConstraint(grid['X' + str(i) + str(j)], grid['X' + str(i) + str(k)], different)

    for j in range(1, column + 1):
        for i in range(1, row + 1):
            for l in range(1, row + 1):
                if grid['X' + str(i) + str(j)] != grid['X' + str(l) + str(j)]:
                    sudoku.addConstraint(grid['X' + str(i) + str(j)], grid['X' + str(l) + str(j)], different)

    for i in range(1, row + 1, 3):
        for j in range(1, column + 1, 3):
            for n in range(i, i + 3):
                for m in range(j, j + 3):
                    for l in range(i, i + 3):
                        for k in range(j, j + 3):
                            if (grid['X' + str(n) + str(m)] != grid['X' + str(l) + str(k)]):
                                sudoku.addConstraint(grid['X' + str(n) + str(m)], grid['X' + str(l) + str(k)],
                                                     different)

    print('find a solution...')
    result = cutsetConditioning(sudoku)

    if result is not None:
        for var in result.getAssignment():
            values[int(var.getVariableName()[1]) - 1][int(var.getVariableName()[2]) - 1] = result.getAssignment()[var]
        printGrid(values)
    else:
        print('UNSATISFACTABLE PROBLEM')
    print('-----------------------------------')

    print('SUDOKU 2')
    sudoku = CSP()
    domainSudoku = Domain([1, 2, 3, 4, 5, 6, 7, 8, 9])
    different = Constraint(lambda a, b: a != b, '≠')

    row = 9
    column = 9
    cell = 3
    grid = {}
    values = [
        [0, 8, 0, 0, 0, 9, 7, 4, 3],
        [0, 5, 0, 0, 0, 8, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 8, 0, 4, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 6],
        [0, 7, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 5, 0, 0, 0, 8, 0],
        [9, 7, 2, 4, 0, 0, 0, 5, 0]
    ]
    printGrid(values)

    for i in range(1, row + 1):
        for j in range(1, column + 1):
            if values[i - 1][j - 1] != 0:
                grid["X{0}{1}".format(i, j)] = Variable('X' + str(i) + str(j), Domain([values[i - 1][j - 1]]))
            else:
                grid["X{0}{1}".format(i, j)] = Variable('X' + str(i) + str(j), domainSudoku)

    print('Instanziate region as variables...')
    for i in range(1, row + 1):
        for j in range(1, row + 1):
            sudoku.addVariable(grid['X' + str(i) + str(j)])

    print('Instanziate costraints...')
    for i in range(1, row + 1):
        for j in range(1, column + 1):
            for k in range(1, column + 1):
                if grid['X' + str(i) + str(j)] != grid['X' + str(i) + str(k)]:
                    sudoku.addConstraint(grid['X' + str(i) + str(j)], grid['X' + str(i) + str(k)], different)

    for j in range(1, column + 1):
        for i in range(1, row + 1):
            for l in range(1, row + 1):
                if grid['X' + str(i) + str(j)] != grid['X' + str(l) + str(j)]:
                    sudoku.addConstraint(grid['X' + str(i) + str(j)], grid['X' + str(l) + str(j)], different)

    for i in range(1, row + 1, 3):
        for j in range(1, column + 1, 3):
            for n in range(i, i + 3):
                for m in range(j, j + 3):
                    for l in range(i, i + 3):
                        for k in range(j, j + 3):
                            if (grid['X' + str(n) + str(m)] != grid['X' + str(l) + str(k)]):
                                sudoku.addConstraint(grid['X' + str(n) + str(m)], grid['X' + str(l) + str(k)],
                                                     different)

    print('find a solution...')
    result = cutsetConditioning(sudoku)

    if result is not None:
        for var in result.getAssignment():
            values[int(var.getVariableName()[1]) - 1][int(var.getVariableName()[2]) - 1] = result.getAssignment()[var]
        printGrid(values)
    else:
        print('UNSATISFACTABLE PROBLEM')
    print('-----------------------------------')
