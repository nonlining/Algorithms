#Uses python2

def lcs3(a, b, c):
    m = len(a)
    n = len(b)
    o = len(c)
    D = [[[0 for k in xrange(n+1)] for j in xrange(m+1)] for i in xrange(o+1)]

    for k in range(0, o):
        for i in range(0,m):
            for j in range(0,n):

                if a[i] == b[j] == c[k]:
                    D[k+1][i+1][j+1] = D[k][i][j] + 1
                else:
                    D[k+1][i+1][j+1] = max(D[k][i+1][j+1], D[k+1][i+1][j], D[k+1][i][j+1])
    return D[o][m][n]


def lcs2(s, t):
  m = len(s)
  n = len(t)
  D = [x[:] for x in [[0] * (n+1)] * (m+1)]
  reCon = []
  for i in range(0,m):
    for j in range(0,n):
        if s[i] == t[j]:
            D[i+1][j+1] = D[i][j+1] + 1
        else:
            D[i+1][j+1] = max(D[i+1][j], D[i][j+1])
  LCS_len = D[m][n]

  sm = m
  tn = n
  while LCS_len > 0 and sm > 0 and tn > 0:

    if s[sm-1] == t[tn-1]:
        reCon.append(s[sm-1])
        if D[sm-1][tn] == LCS_len - 1:
            LCS_len -= 1
            sm -= 1
        elif D[sm][tn-1] == LCS_len - 1:
            LCS_len -= 1
            tn-=1

    else:
        if D[sm-1][tn] == LCS_len:
            sm -= 1
        elif D[sm][tn-1] == LCS_len:
            tn-=1

  reCon.reverse()
  return reCon

if __name__ == "__main__":
    n = int(raw_input())
    lst1 = map(int, raw_input().split(' '))
    n = int(raw_input())
    lst2 = map(int, raw_input().split(' '))
    n = int(raw_input())
    lst3 = map(int, raw_input().split(' '))
    #lst1 = [8,3,2,1,7,9]
    #lst2 = [8,2,1,3,8,10,7]
    #lst3 = [6,8,3,1,4,7]
    print lcs3(lst1, lst2, lst3)

