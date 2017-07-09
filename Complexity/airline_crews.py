# python2

def dfs(adj_matrix, u, matchR, seen, matchP):

    for v in range(len(seen)):
        if adj_matrix[u][v] and seen[v] == False:
            seen[v] = True
            if matchR[v] == -1 or bpm(adj_matrix, matchR[v], matchR, seen, matchP):
                matchR[v] = u
                matchP[u] = v
                return

def bfs(adj_matrix, u, matchR, seen, matchP):
    queue=[]

    queue.append(u)
    while queue:
        u = queue.pop(0)
        for ind, val in enumerate(adj_matrix[u]):
            if seen[ind] == False and val > 0 :
                if matchR[ind] == -1:
                    seen[ind] = True
                    matchR[ind] = u
                    matchP[u] = ind
                    return
                else:
                    queue.append(matchR[ind])
                    matchR[ind] = u
                    matchP[u] = ind

class MaxMatching:
    def read_data(self):
        n, m = map(int, raw_input().split())
        adj_matrix = [list(map(int, raw_input().split())) for i in range(n)]
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))

    def find_matching(self, adj_matrix):

        n = len(adj_matrix) # crew
        m = len(adj_matrix[0]) # flights
        matchR = [-1] * m
        match = [-1] * n

        for i in range(n):
            seen = [False] * m
            dfs(adj_matrix, i, matchR, seen, match)
            #bfs(adj_matrix, i, matchR, seen, match)

        return match

    def solve(self):
        adj_matrix = self.read_data()
        matching = self.find_matching(adj_matrix)
        self.write_response(matching)

if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
