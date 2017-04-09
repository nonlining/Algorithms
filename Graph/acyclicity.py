#Uses python3

import sys

def dfs(adj, path, visited, v):
    if v in path:
        return 1
    visited[v] = 1
    path.add(v)
    for e in adj[v]:
        if (dfs(adj, path, visited, e)):
            return 1
    path.remove(v)
    return 0

def acyclic(adj):
    visited = [0] * len(adj)
    path = set()
    for i in range(len(adj)):
        if(visited[i] == 0 and dfs(adj, path, visited, i)):
            return 1
    return 0

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())


    adj = [[] for _ in range(n)]

    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        adj[a - 1].append(b - 1)

    print(acyclic(adj))
