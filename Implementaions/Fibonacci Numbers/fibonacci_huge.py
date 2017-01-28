# Uses python2
import sys

def get_fibonacci_huge2(n, m):
    v1, v2, v3 = 1, 1, 0

    for rec in bin(n)[3:]:
        calc = (v2*v2) % m
        v1, v2, v3 = (v1*v1+calc) % m, ((v1+v3)*v2) % m, (calc+v3*v3) % m
        if rec == '1': v1, v2, v3 = (v1+v2) % m, v1, v2
    return v2



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

if __name__ == '__main__':

    n, m = map(int, raw_input().split(' '))
    print get_fibonacci_huge(n, m)
    #print get_fibonacci_huge2(n, m)
