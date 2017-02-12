#Uses python2

def MergeSortedArray(lst1 ,lst2):

    Res = []
    lst1Len = 0
    lst2Len = 0
    cp = 0

    while lst1Len < len(lst1) and lst2Len < len(lst2):

        if lst1[lst1Len] <= lst2[lst2Len]:
            Res.append(lst1[lst1Len])
            lst1Len += 1
        else:
            Res.append(lst2[lst2Len])

            cp += len(lst1) - lst1Len
            lst2Len += 1

    if lst1Len < len(lst1):
        Res.extend(lst1[lst1Len:])

    if lst2Len < len(lst2):
        Res.extend(lst2[lst2Len:])

    return Res, cp


def mergeSort(data, n):
    cp = 0
    if n == 1:
        return data, cp

    a = data[:n/2]
    b = data[n/2:]

    ma, na= mergeSort(a, len(a))
    mb, nb = mergeSort(b, len(b))

    res,cp = MergeSortedArray(ma, mb)

    return (res, cp + na + nb)



def minimum_distance(data, n):
    res, cp = mergeSort(data, n)

    return cp

if __name__ == '__main__':
    n = int(raw_input())
    data = map(int, raw_input().split(' '))
    #n = 6
    #data = [9, 8, 7, 3, 2, 1]
    # 15
    print minimum_distance(data, n)

