# Uses python2

import random
from random import shuffle


def partition3(a, l, r):
    j = l
    i = l
    k = r
    pivot = a[l]

    while i <= k:
        if a[i] < pivot:
            a[j], a[i] = a[i], a[j]
            j += 1
            i += 1
        elif a[i] > pivot:
            a[i], a[k] = a[k], a[i]
            k -= 1
        else:
            i += 1

    return j, k

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            print i, j
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def partition(a, l, r):
    j = l
    i = l+1
    k = r
    pivot = a[l]

    while i <= k:
        if a[i] <= pivot:
            j += 1
            a[j], a[i] = a[i], a[j]
        i += 1
    a[l], a[j] = a[j], a[l]

    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)

    a[l], a[k] = a[k], a[l]
    m, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m2 + 1, r);

def randomized_quick_sort2(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m = partition2(a, l, r)
    randomized_quick_sort2(a, l, m - 1);
    randomized_quick_sort2(a, m + 1, r);



if __name__ == '__main__':
    n = int(raw_input())
    a = map(int, raw_input().split(' '))
    #n = random.randint(1, 20)
    #a = [2, 3, 8, 10, 2, 8, 9, 9, 0, 11, 1]
    #n = len(a)
    #a2 = a
    randomized_quick_sort(a, 0, n - 1)
    #randomized_quick_sort2(a2, 0, n - 1)


    for x in a:
        print x,
