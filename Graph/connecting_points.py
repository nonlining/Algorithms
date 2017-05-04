#Uses python3
import sys
import math
import heapq

def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


def minimum_distance(adj, weight):
    result = 0.
    dist = [float('inf')]*len(adj)
    dist[0] = 0
    visited = set()

    cost = [(i,d) for d, i in enumerate(dist)]

    visited.add(0)
    heapq.heapify(cost)

    while len(cost) != 0:
        u = cost[0]

        visited.add(u[1])

        heapq.heappop(cost)

        for v in adj[u[1]]:
            if (v not in visited and dist[v] > weight[u[1]][v]) :
                dist[v] = weight[u[1]][v]
                cost = [(i,d) for d, i in enumerate(dist)]
                heapq.heapify(cost)

    return sum(dist)



if __name__ == '__main__':

    n = int(sys.stdin.readline())
    x = []
    y = []
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        x.append(a)
        y.append(b)

    adj = [[] for _ in range(n)]
    weight = [[0]*n for _ in range(n)]
    for i in range(n):
        adj[i] = list(v for v in range(n) if v != i)
        for j in range(n):
            if i != j:
                w = dist(x[i], y[i], x[j], y[j])
                weight[i][j] = w
                weight[j][i] = w

    print("{0:.9f}".format(minimum_distance(adj, weight)))
