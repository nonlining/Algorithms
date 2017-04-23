#Uses python3

import sys

def negative_cycle(adj, cost):
    dist = [9223372036854775807] * len(adj)
    dist[0] = 0

    for _ in range(len(adj)):
        for u in range(len(adj)):
            for i, v in enumerate(adj[u]):
                if dist[v] > dist[u] + cost[u][i]:
                    dist[v] = dist[u] + cost[u][i]
                    if _ == len(adj) - 1:
                        return 1

    return 0

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())

    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for _ in range(m):
        a, b, w = map(int, sys.stdin.readline().split())
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)

    print(negative_cycle(adj, cost))
