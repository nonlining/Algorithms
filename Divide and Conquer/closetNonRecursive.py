#Uses python3
import math
import sys
from collections import deque

def distance(p1, p2):
    return math.sqrt((p1[0]- p2[0])**2+(p1[1]- p2[1])**2)

def b_force(points, start, end):
    localMin = float('inf')
    if (end - start) < 4:
        for i in range(start, end):
            for j in range(i+1, end):
                localMin = min(localMin, distance(points[i], points[j]))
    return localMin


def min_distance(points):
    start = 0
    end = len(points)
    step = 2
    q = deque()
    tempq = deque()

    while start < end:
        if step + start < end:
            if step + start + 1 == end:
                temp = b_force(points, start, step + start + 1)
                q.append((temp,(start,step + start + 1)))
                break
            else:
                temp = b_force(points, start, step + start)
                q.append((temp,(start, step + start)))
        else:
            temp = b_force(points, start, step + start)
            q.append((temp,(start, step + start)))

        start += step

    minD = 0
    while len(q) > 0:
        l = q.popleft()
        start = l[1][0]
        end = l[1][1]
        minD = l[0]

        if len(q):
            r = q.popleft()
            end = r[1][1]
            minD = min(r[0], minD)

        mid = start + (end - start)//2
        midPoint = points[mid]
        closetToMidLine = []

        for i in range(start ,end):
            if abs(midPoint[0] - points[i][0]) < minD:
                closetToMidLine.append(points[i])

        tempMin = minD
        closetToMidLine.sort(key=lambda x : (x[1],x[0]))
        for i in range(len(closetToMidLine)):
            maxTry = 0
            for j in range(i+1, len(closetToMidLine)):
                if maxTry > 3:
                    break
                tempMin = min(tempMin, distance(closetToMidLine[i],closetToMidLine[j]))
                maxTry += 1
        minD = min(tempMin,minD)
        tempq.append((minD, (start, end)))
        if len(q) == 0:
            q.extend(tempq)
            tempq.clear()
        if len(q) == 1 and len(tempq) == 0:
            break
    return q.popleft()[0]




if __name__ == '__main__':
    # test case
    #x = [4,-2,-3,-1,2,-4,1,-1,3,-4,-2]
    #y = [4,-2,-4,3,3,0,1,-1,-1,2,4]
    #x = [7, 1, 4, 7]
    #y = [7, 100, 8, 7]
    #x = [0 ,3]
    #y = [0 ,4]
    #x = [2, -59, -93, -7, 32, 45, -16, -78, 77, 63, 82, -75, -74, -73]
    #y = [40, -82, -19, -19, 81, -14, -15, -35, 89, 77, 84, 2, 38, -3]

    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]

    points = zip(x, y)
    points = sorted(points, key=lambda x : (x[0],x[1]))
    res = min_distance(points)
    print("{0:.9f}".format(res))
