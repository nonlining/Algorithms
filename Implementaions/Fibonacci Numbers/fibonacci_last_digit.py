# Uses python2
def calc_fib(n):
    if n <= 1:
        return n

    prev = 0
    current = 1
    for i in range(2,n+1):
        current, prev = (prev + current)%10, current

    return current

n = int(raw_input())
print calc_fib(n)
