#Uses python3

import sys
from collections import deque

def bipartite(adj):
    s = 0
    t = len(adj) - 1

    q = deque()
    visited = [-1] * len(adj)
    visited[s] = 0

    q.append(s)
    while len(q)!= 0:
        p = q.popleft()
        c = 0 if (visited[p]) else 1
        for e in adj[p]:
            if visited[e] == -1:
                q.append(e)
                visited[e] = c
            elif visited[e] == visited[p]:
                return 0

    return 1

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())

    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    print(bipartite(adj))
