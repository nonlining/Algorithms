#Uses python3
import sys
import math

def minimum_distance(x, y):
    result = 0.
    #write your code here
    return result


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    x = []
    y = []
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        x.append(a)
        y.append(b)
    print("{0:.9f}".format(minimum_distance(x, y)))
