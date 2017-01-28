# Uses python2
import sys

def gcd(a, b):
    if(b == 0):
        return a
    return gcd(b , a%b)


def lcm_naive(a, b):
    g = 1
    if a > b:
        g = gcd(a, b)
    else:
        g = gcd(b, a)

    return a*b/g

if __name__ == '__main__':
    a, b = map(int, raw_input().split(' '))
    print lcm_naive(a, b)

