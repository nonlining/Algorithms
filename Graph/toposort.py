#Uses python3

import sys

def dfs(adj, used, order, x):
    if used[x] == 1:
        return
    used[x] = 1
    for e in adj[x]:
        if used[e] == 0:
            dfs(adj, used, order, e)
    order.append(x)


def toposort(adj):
    used = [0] * len(adj)
    order = []
    for v in range(len(adj)):
        dfs(adj, used, order, v)
    return reversed(order)

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        adj[a - 1].append(b - 1)

    order = toposort(adj)

    for x in order:
        print(x + 1, end=' ')

