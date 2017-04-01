#Uses python3
import sys

def reach(adj, x, y, visited):
    visited[x] = 1
    for e in adj[x]:
        if e == y:
            visited[e] = 1
            return 1
        if (visited[e] != 1):
            reach(adj, e, y, visited)

    return 1 if visited[y] == 1 else 0


if __name__ == '__main__':

    n, m = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n)]
    visited = [0] * n

    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    x, y = map(int, sys.stdin.readline().split())
    x, y = x - 1, y - 1

    print(reach(adj, x, y, visited))


