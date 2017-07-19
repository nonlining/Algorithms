# python2

EPS = 1e-6
PRECISION = 20

class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row

def ReadEquation():
    size = int(raw_input())
    a = []
    b = []
    for row in range(size):
        line = map(float, raw_input().split(' '))
        a.append(line[:size])
        b.append(line[size])

    return Equation(a, b)

def SelectPivotElement(a, used_rows, used_columns):

    pivot_element = Position(0, 0)
    while used_rows[pivot_element.row]:
        pivot_element.row += 1
    while used_columns[pivot_element.column]:
        pivot_element.column += 1

    maxEl = abs(a[pivot_element.row][pivot_element.column])
    maxRow = pivot_element.row
    for k in range(pivot_element.row, len(a)):
        if abs(a[k][pivot_element.column]) > maxEl:
            maxEl = abs(a[k][pivot_element.column])
            maxRow = k
    pivot_element.row = maxRow
    return pivot_element

def SwapLines(a, b, used_rows, pivot_element):

    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
    pivot_element.row = pivot_element.column;


def ProcessPivotElement(a, b, pivot_element):

    n = len(a)
    for k in range(pivot_element.row+1, n):
        c = -a[k][pivot_element.column]/a[pivot_element.row][pivot_element.column]
        for j in range(pivot_element.row, n):
            if pivot_element.row == j:
                a[k][j] = 0
            else:
                a[k][j] += c * a[pivot_element.row][j]

        b[k] += c*b[pivot_element.row]

def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True

def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)

    used_columns = [False] * size
    used_rows = [False] * size
    for step in range(size):
        pivot_element = SelectPivotElement(a, used_rows, used_columns)
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)

    x = [0 for i in range(len(a))]
    for i in range(len(a) -1 , -1 , -1):
        b[i] = b[i]/a[i][i]
        for k in range(i-1, -1, -1):
            b[k] -= a[k][i]*b[i]

    return b

def PrintColumn(column):
    size = len(column)
    for row in range(size):
        print("%.6f" % column[row]),

if __name__ == "__main__":
    equation = ReadEquation()
    solution = SolveEquation(equation)
    PrintColumn(solution)
