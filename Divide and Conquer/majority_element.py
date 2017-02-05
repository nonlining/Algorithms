# Uses python2


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    return -1

def get_majority(a):
    cand = -1
    count = 0

    for i in a:
        if count == 0:
            count = 1
            cand = i
        else:
            if cand == i:
                count = count + 1
            else:
                count = count - 1
    count = 0

    for i in a:
        if cand == i:
            count = count + 1
    if count > (len(a)/2):
        return 1

    return -1

if __name__ == '__main__':
    n = int(raw_input())
    a = map(int, raw_input().split(' '))

    if get_majority(a) != -1:
        print 1
    else:
        print 0
