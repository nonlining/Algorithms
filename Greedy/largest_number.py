#Uses python2


numOfDigits = dict()

def howmanydigits(a):
    num = a
    count = 0
    while(num):
        num =num/10
        count = count + 1
    return count


def compare(a ,b):
    num_d_a = numOfDigits[a]
    num_d_b = numOfDigits[b]
    if num_d_a == num_d_b:
        return a > b
    else:
        first =  a*10**num_d_b + b
        second =  b*10**num_d_a + a
        return first > second

def partition(lst, b, e, index):
    if len(lst) == 0:
        return lst, -1
    if e < b:
        return lst, -1
    indexValue = lst[index]
    lst[e-1], lst[index] = lst[index],lst[e-1]
    start =b

    for i in range(b,e):
        #if lst[i] > indexValue:
         if compare(lst[i], indexValue):
            lst[start], lst[i] = lst[i],lst[start]
            start = start +1
    lst[start], lst[e-1] = lst[e-1],lst[start]

    return lst, start



def QuickSort(lst, begin , end):
    if begin < end :
        # choice pivot , this uses middle as pivot
        med = begin + (end - begin) /2
        lst , newMed = partition(lst, begin , end , med )
        QuickSort(lst, begin ,newMed)
        QuickSort(lst,newMed + 1, end)
    return lst



def largest_number(a):
    l = 0
    r = len(a)
    for i in a:
        numOfDigits[i] = howmanydigits(i)
    a = QuickSort(a, l ,r)

    res = 0
    for i in range(len(a)):
        res = res*10**numOfDigits[a[i]] + a[i]

    return res

if __name__ == '__main__':
    n = int(raw_input())
    a = map(int, raw_input().split(' '))

    print largest_number(a)

