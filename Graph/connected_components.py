#Uses python3
import sys

def DFS(adj, x, visited):
    visited[x] = 1
    for e in adj[x]:
        if (visited[e] != 1):
            DFS(adj, e, visited)


def number_of_components(adj, x, visited):
    result = 0

    for v in range(len(adj)):
        if (visited[v] != 1):
            DFS(adj, v, visited)
            result += 1

    return result

if __name__ == '__main__':

    n, m = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n)]
    visited = [0] * n
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)


    print(number_of_components(adj, 0, visited))
