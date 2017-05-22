# python2
import sys

def InverseBWT3(bwt):
    sort_index = sorted(range(len(bwt)), key=lambda x: bwt[x])
    index = 0
    text = ""
    sorted_bwt = sorted(bwt)
    for i, e in enumerate(sort_index):
        text = text + sorted_bwt[sort_index[index]]
        index = sort_index[index]
    return text


def InverseBWT2(bwt):
    n = len(bwt)
    m = sorted(bwt)
    for j in range(n-1):
        for i in range(n):
            m[i] = bwt[i]+m[i]

        m = sorted(m)

    return m[0][1:]+'$'

def InverseBWT(bwt):
    n = len(bwt)
    counter = {}
    map = {}
    last = []
    c = 0
    for i in bwt:
        if i in counter:
            counter[i]+=1
            last.append(i + " " +str(counter[i]))
        else:
            counter[i] = 1
            last.append(i + " " +str(counter[i]))
        map[i + " " +str(counter[i])] = c
        c += 1

    first = [v[0] for v in sorted(map.iteritems(), key=lambda(k, v): (k[0], v))]

    index = 0
    text = ""
    for i in range(n-1):
        letter = last[index]

        text = letter[0] + text
        index = first.index(letter)

    return text+'$'


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    #bwt =  "AAAC$CGAAAAAAAACCCCAAGA"
    #print(InverseBWT2(bwt))
    #print(InverseBWT(bwt))
    print(InverseBWT3(bwt))