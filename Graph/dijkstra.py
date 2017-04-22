#Uses python3

import sys
#import queue
import heapq


def distance(adj, cost, s, t):
    dist = [float('inf')]*len(adj)
    prev = [None]*len(adj)
    dist[s] = 0
    q = [(i,d) for d, i in enumerate(dist)]

    heapq.heapify(q)

    while len(q) != 0:
        u = q[0]
        heapq.heappop(q)
        #print q
        for i, e in enumerate(adj[u[1]]):
            #print u, u[1]+1, e+1, dist[e], cost[u[1]][i]
            if dist[e] > dist[u[1]] + cost[u[1]][i]:
                dist[e] = dist[u[1]] + cost[u[1]][i]
                q = [(i,d) for d, i in enumerate(dist)]
                heapq.heapify(q)

    return dist[t] if dist[t] != float('inf') else -1


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())

    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for _ in range(m):
        a, b, w = map(int, sys.stdin.readline().split())
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = map(int, sys.stdin.readline().split())
    print(distance(adj, cost, s-1, t-1))
