# Uses python2

def evalt(a, b, op):
    #print 'evalt', a, op, b
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False
def MinAndMax(i, j, m, M, dataset):
    min_value = float('inf')
    max_value = float('-inf')
    for k in range(i, j):
        #print M[i][k],m[k+1][j], dataset[2*k+1]
        a = evalt(M[i][k], M[k+1][j], dataset[2*k+1])
        b = evalt(M[i][k], m[k+1][j], dataset[2*k+1])
        c = evalt(m[i][k], M[k+1][j], dataset[2*k+1])
        d = evalt(m[i][k], m[k+1][j], dataset[2*k+1])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
    #print 'm, M', min_value,max_value
    return min_value, max_value

def get_maximum_value(dataset):
    n = len(dataset)/2 + 1
    #print n
    m = [x[:] for x in [[0] * (n)] * (n)]
    M = [x[:] for x in [[0] * (n)] * (n)]

    for i in range(n):
        m[i][i] = int(dataset[2*i])
        M[i][i] = int(dataset[2*i])
    for s in range(1,n):
        for i in range(0,n-s):
            j = i + s
            #print 'index ',i,j
            m[i][j], M[i][j] = MinAndMax(i, j, m, M, dataset)

    return M[0][n-1]


if __name__ == "__main__":
    exp = raw_input()
    print get_maximum_value(exp)
