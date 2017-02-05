# Uses python2
import sys

def binary_search(a, x):
    left, right = 0, len(a)

    while left < right:
        mid = left + (right - left)/2
        if a[mid] == x:
            return mid
        elif a[mid] > x:
            right = mid
        elif a[mid] < x:
            left = mid + 1

    return -1
def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':

    data = map(int, raw_input().split(' '))
    data2 = map(int, raw_input().split(' '))
    n = data[0]
    a = data[1 : n + 1]
    m = data2[0]

    #for x in data2[1:]:
        # replace with the call to binary_search when implemented
    #    print linear_search(a, x),

    for x in data2[1:]:
        # replace with the call to binary_search when implemented
        print binary_search(a, x),