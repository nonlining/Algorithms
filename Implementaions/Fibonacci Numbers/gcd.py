# Uses python2
import sys

def gcd(a, b):
    if(b == 0):
        return a
    return gcd(b , a%b)

if __name__ == "__main__":
    a, b = map(int, raw_input().split(' '))
    if a > b:
        print gcd(a, b)
    else:
        print gcd(b, a)



