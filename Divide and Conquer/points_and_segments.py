# Uses python2

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    lst = zip(starts, [-1]*len(starts))
    lst.extend(zip(ends, [len(points)+1]*len(starts)))
    lst.extend(zip(points, range(len(points))))
    lst.sort(key=lambda x : (x[0],x[1]))

    stk = []
    for i in lst:
        if i[1] == -1:
            stk.append(i)
        elif i[1] == len(points)+1:
            stk.pop()
        else:
            cnt[i[1]] = len(stk)

    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    n, l = map(int, raw_input().split(' '))
    starts = []
    ends = []

    while n > 0:
        s, e = map(int, raw_input().split(' '))
        starts.append(s)
        ends.append(e)
        n -= 1

    points = map(int, raw_input().split(' '))

    cnt = fast_count_segments(starts, ends, points)
    #cnt1 = naive_count_segments(starts, ends, points)
    #print cnt
    #print cnt1

    for x in cnt:
        print x,
