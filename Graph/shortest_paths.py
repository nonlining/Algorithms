#Uses python3
import sys
#import queue
import heapq


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    n = len(adj)
    distance[s] = 0
    reachable[s] = 1
    queue = []
    visited = [0]*n

    for iter in range(n):
        for u in range(n):
            for i, v in enumerate(adj[u]):
                if distance[v] > distance[u] + cost[u][i]:
                    if iter < n-1:
                        distance[v] = distance[u] + cost[u][i]
                        reachable[v] = 1
                    else:
                        if v not in queue:
                            queue.append(v)
    heapq.heapify(queue)

    while len(queue) != 0:
        u = queue[0]
        heapq.heappop(queue)

        visited[u] = True
        shortest[u] = 0
        for v in adj[u]:
            if not visited[v] and v not in queue:
                queue.append(v)
                heapq.heapify(queue)


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())

    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for _ in range(m):
        a, b, w = map(int, sys.stdin.readline().split())
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)

    s = int(sys.stdin.readline())
    s -= 1

    distance = [float('inf')] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])
