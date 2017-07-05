# python2

class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow


def read_data():
    vertex_count, edge_count = map(int, raw_input().strip().split(' '))

    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, raw_input().strip().split(' '))
        graph.add_edge(u - 1, v - 1, capacity)
    return graph


def BFS(graph, s, t, parent, pathIds):

    visited =[False]*(graph.size())
    queue=[]

    queue.append(s)
    visited[s] = True

    while queue:
        u = queue.pop(0)
        for _ , val in enumerate(graph.get_ids(u)):

            ind = graph.get_edge(val).v


            if visited[ind] == False and graph.get_edge(val).capacity - graph.get_edge(val).flow > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
                pathIds[ind] = val

    return True if visited[t] else False

def max_flow(graph, from_, to):
    flow = 0

    pre = [-1] * graph.size()
    pathIds = [-1] * graph.size()
    count = 0

    while(BFS(graph, from_, to, pre, pathIds)):

        path_flow = float("Inf")
        s = to
        while(s !=  from_):

            path_flow = min (path_flow, graph.get_edge(pathIds[s]).capacity - graph.get_edge(pathIds[s]).flow)
            s = pre[s]

        flow += path_flow
        v = to
        while(v != from_):

            graph.add_flow(pathIds[v], path_flow)
            v = pre[v]

        pre = [-1] * graph.size()
        pathIds = [-1] * graph.size()


    return flow


if __name__ == '__main__':
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))
