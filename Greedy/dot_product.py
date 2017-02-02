#Uses python2

def max_dot_product(a, b):
    a.sort()
    b.sort()
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    n = int(raw_input())
    a = map(int, raw_input().split(' '))
    b = map(int, raw_input().split(' '))

    print max_dot_product(a, b)

