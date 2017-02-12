# Uses python2
def edit_distance(s, t):
  m = len(s)
  n = len(t)
  D = [x[:] for x in [[0] * (n+1)] * (m+1)]
  for i in range(n+1):
    D[0][i] = i

  for i in range(m+1):
    D[i][0] = i

  for i in range(1,m+1):
    for j in range(1,n+1):
      D[i][j] = min( D[i-1][j]+1, D[i][j-1]+1,
        D[i-1][j-1] + apply(lambda: 0 if s[i-1] == t[j-1] else 1))

  return D[m][n]

if __name__ == "__main__":
    str1 = raw_input()
    str2 = raw_input()
    print edit_distance(str1, str2)
