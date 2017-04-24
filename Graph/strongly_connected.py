#Uses python3

import sys

sys.setrecursionlimit(200000)

def reverseEdges(adj):
    r_adj = [[] for _ in range(len(adj))]
    for v in range(len(adj)):
        for e in adj[v]:
            r_adj[e].append(v)
    return r_adj


def dfs(adj, used, x, order = []):
    if used[x] == 1:
        return

    used[x] = 1
    for e in adj[x]:
        if not used[e]:
            dfs(adj, used, e, order)
    order.append(x)


def number_of_strongly_connected_components(adj):
    result = 0
    order = []
    used = [0]*len(adj)

    for v in range(len(adj)):
        dfs(adj, used, v, order)


    r_adj = reverseEdges(adj)

    used = [0]*len(adj)

    while order:
        v = order.pop()
        if not used[v]:
            dfs(r_adj, used, v)
            result += 1



    return result

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
