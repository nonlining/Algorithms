# Uses python2

def get_optimal_value(capacity, weights, values):

    value = 0.
    vw = []
    for i in range(len(values)):
        vw.append(values[i]/float(weights[i]))
    vw_Wlist = zip(vw, weights)

    vw_Wlist.sort(key = lambda t: t[0])

    for i in range(len(vw)-1, -1, -1):
        if capacity > 0:
            m = min(capacity, vw_Wlist[i][1])
            capacity = capacity - m
            value = value + m*vw_Wlist[i][0]
        elif capacity == 0:
            break


    return value


if __name__ == "__main__":
    n, capacity = map(int, raw_input().split(' '))
    count = n
    values = []
    weights = []
    while(count):
        v, w = map(int, raw_input().split(' '))
        values.append(v)
        weights.append(w)
        count = count - 1

    opt_value = get_optimal_value(capacity, weights, values)

    print("{:.4f}".format(opt_value))
