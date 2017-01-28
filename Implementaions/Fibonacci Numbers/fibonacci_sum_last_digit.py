# Uses python2
import math

def fibonacci_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current)%10

    return current


def get_fibonacci_huge(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    prevMod = -1
    currMod = -1
    counter = 0
    piN = -1

    while counter < n-1:
        previous, current = current, previous + current
        currMod = current%m
        counter = counter + 1

        if(prevMod == 0 and currMod == 1):
            piN = counter
            break
        prevMod = currMod

    if piN > 0:
        new_n = n%piN
        if new_n <= 1:
            return new_n
        previous = 0
        current  = 1
        for _ in range(new_n-1):
            previous, current = current, previous + current
        return current%m
    else:
        return current%m

def fibonacci_sum(n):
    if n <= 1:
        return n

    sum = get_fibonacci_huge(n+2, 10) - 1
    if sum == -1:
        return 9

    return sum%10

if __name__ == '__main__':
    n = int(raw_input())

    print fibonacci_sum(n)
