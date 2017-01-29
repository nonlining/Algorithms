# Uses python2

def get_change(m):
    #write your code here
    numsCoin = 0
    coins = [10, 5, 1]
    for i in coins:
        if i <= m:
            numsCoin = numsCoin + m/i
            m = m - i*(m/i)
    m = numsCoin

    return m

if __name__ == '__main__':
    m = int(raw_input())
    print get_change(m)
