# Uses python2
def fibonacci_partial_sum_naive(from_, to):
    if to <= 1:
        return to

    previous = 0
    current  = 1

    for _ in range(from_ - 1):
        previous, current = current, previous + current

    sum = current

    for _ in range(to - from_):
        previous, current = current, previous + current
        sum += current

    return sum % 10

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

def fibonacci_partial_sum(f, t):
    fsum = get_fibonacci_huge(f+1, 10) - 1
    tsum = get_fibonacci_huge(t+2, 10) - 1

    sum = tsum - fsum

    if sum < 0:
        sum = sum + 10

    return sum%10



if __name__ == '__main__':

    f, t = map(int, raw_input().split(' '))
    print fibonacci_partial_sum(f, t)
