# python2
import sys

n, m =  map(int, sys.stdin.readline().split())
lines = [int(s) for s in raw_input().split(' ')]
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

def getParent(table):
    if table != parent[table]:
        parent[table] = getParent(parent[table])
    return parent[table]

def merge(destination, source):
    global ans

    PX, PY = getParent(destination), getParent(source)

    if PX == PY:
        return False

    if(rank[PX] > rank[PY]):
        parent[PY] = PX
        lines[PX] += lines[PY]
        lines[PY] = 0
    else:
        parent[PX] = PY
        lines[PY] += lines[PX]
        lines[PX] = 0
        if (rank[PX] == rank[PY]):
            rank[PY] = rank[PY] + 1

    ans = max(ans, lines[PX], lines[PY])
    return True

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)

    print(ans)

