# Uses python2
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    if len(segments) ==1:
        points.append(segments[0].end)

    segments.sort(key = lambda x : x.end)
    i = 0
    j = i + 1
    while i < len(segments):
        minEndPoint = segments[i].end
        points.append(minEndPoint)
        if j < len(segments) and minEndPoint < segments[j].start:
            i = i + 1
        while j < len(segments) and minEndPoint >= segments[j].start:
            j = j + 1
            i = j
    return points

if __name__ == '__main__':
    n = int(raw_input())
    segments = []
    while(n):
        data = map(int, raw_input().split(' '))
        segments.append(Segment(data[0], data[1]))
        n = n - 1

    points = optimal_points(segments)

    print len(points)

    for p in points:
        print p,
