# Uses python2
def optimal_summands(n):
    summands = []
    sum = n
    i = 1
    while sum > 0:
        if sum <= i*2:
            summands.append(sum)
            sum = sum - sum
        else:
            summands.append(i)
            sum = sum - i
        i = i + 1

    return summands

if __name__ == '__main__':
    n = int(raw_input().strip())
    summands = optimal_summands(n)
    print len(summands)
    for x in summands:
        print x,