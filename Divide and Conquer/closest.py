#Uses python2

import math
import random


def distance(p1, p2):
    return math.sqrt((p1[0]- p2[0])**2+(p1[1]- p2[1])**2)

def minimum_distance(points):

    if len(points) < 4:
        minD = float('inf')
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                minD = min(minD, distance(points[i], points[j]))
        return minD
    mid = len(points)/2
    l = minimum_distance(points[:mid])
    r = minimum_distance(points[mid:])
    d = min(l,r)
    midPoint = points[mid]

    closetToMidLine = []

    for i in points:
        if abs(midPoint[0] - i[0]) < d:
            print 'd', d, abs(midPoint[0] - i[0]), midPoint, i
            closetToMidLine.append(i)
    tempMin = d
    closetToMidLine.sort(key=lambda x : (x[1],x[0]))
    print closetToMidLine

    for i in range(len(closetToMidLine)):
        maxTry = 0
        for j in range(i+1, len(closetToMidLine)):
            if maxTry > 3:
                break
            print maxTry, closetToMidLine[i], closetToMidLine[j]
            tempMin = min(tempMin, distance(closetToMidLine[i],closetToMidLine[j]))
            maxTry += 1

    d = min(tempMin,d)

    return d

if __name__ == '__main__':
    #n = int(raw_input())
    x = []
    y = []
    #while n:
    #    px, py = map(int, raw_input().split(' '))
    #    x.append(px)
    #    y.append(py)
    #    n -= 1
    x = random.sample(range(0,300), 20)
    y = random.sample(range(0,300), 20)

    points = zip(x, y)
    points.sort(key=lambda x : (x[0],x[1]))

    print("{0:.6f}".format(minimum_distance(points)))
