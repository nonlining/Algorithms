# Uses python2

priDict = {}

def optimal_sequence(n):

    sequence = []
    seqD = [0]*(n+1)

    seqD[1] = 0

    for i in range(2, n+1):
        div3 = float('inf')
        div2 = float('inf')
        min1 = float('inf')
        if i > 0 and i % 3 == 0:
            div3 = seqD[i/3] + 1

        if i > 0 and i % 2 == 0:
            div2 = seqD[i/2] + 1

        min1 = seqD[i-1] + 1
        seqD[i] = min(div3, div2, min1)
    step = seqD[n] - 1
    i = n
    sequence.append(n)
    while(i > 1):
        if step == seqD[i - 1]:
            sequence.append(i-1)
            step -= 1
            i -= 1
        elif i > 0 and i % 3 == 0 and seqD[i/3] == step:
            sequence.append(i/3)
            step -= 1
            i = i/3
        elif i > 0 and i % 2 == 0 and seqD[i/2] == step:
            sequence.append(i/2)
            step -= 1
            i = i/2
    sequence.reverse()
    return sequence

def primitive_sequence(n):

    if n <= 0:
        return 0
    if n == 1:
        return 1

    if n in priDict:
        return priDict[n]

    by2 =float('inf')
    by3 =float('inf')
    min1 =float('inf')
    if n&1 == 0:
        by2 = primitive_sequence(n/2) + 1
    if n%3 == 0:
        by3 = primitive_sequence(n/3) + 1
    min1 = primitive_sequence(n-1) + 1
    priDict[n] = min(by2, by3, min1)

    return priDict[n]


n = int(raw_input())
sequence = optimal_sequence(n)

print(len(sequence) - 1)
for x in sequence:
    print x,
