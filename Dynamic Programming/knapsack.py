# Uses python2

# also called 0/1 Knapsack Problem
def optimal_weight(W, w):
    D = [0]*(W+1)
    result = 0
    for x in w:
        for i in range(W, -1, -1):
            if i >= x :
                D[i] = max(D[i], D[i - x]+x)

    return D[W]

if __name__ == '__main__':
    W, n = map(int, raw_input().split(' '))
    w = map(int, raw_input().split(' '))

    print optimal_weight(W, w)
