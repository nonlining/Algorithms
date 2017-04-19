#Uses python3

import sys
#import queue
from collections import deque

def distance(adj, s, t):
    q = deque()
    dist = [-1] * len(adj)
    dist[s-1] = 0
    q.append(s-1)
    while len(q)!= 0:
        p = q.popleft()
        for e in adj[p]:
            if dist[e] == -1:
                q.append(e)
                dist[e] = dist[p] + 1

    return dist[t-1]

if __name__ == '__main__':

    n, m = map(int, sys.stdin.readline().split())

    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = map(int, sys.stdin.readline().split())
    print(distance(adj, s, t))
