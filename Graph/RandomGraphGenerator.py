#-------------------------------------------------------------------------------
# Name:        Generating Random graph.
# Purpose:     This module can be used in algorithm verification.
#
# Author:      Nonlining
#
# Created:     12/09/2016
# Copyright:   (c) Nonlining 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random as rd
import math

def nCr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = dict()
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)
    self.edges[value] = list()

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance

  def getNeighbors(self, node):
    return self.edges[node]


# reference for dijskra for future implementation
##def dijsktra(graph, initial):
##  visited = {initial: 0}
##  path = {}
##
##  nodes = set(graph.nodes)
##
##  while nodes:
##    min_node = None
##    for node in nodes:
##      if node in visited:
##        if min_node is None:
##          min_node = node
##        elif visited[node] < visited[min_node]:
##          min_node = node
##
##    if min_node is None:
##      break
##
##    nodes.remove(min_node)
##    current_weight = visited[min_node]
##
##    for edge in graph.edges[min_node]:
##      weight = current_weight + graph.distance[(min_node, edge)]
##      if edge not in visited or weight < visited[edge]:
##        visited[edge] = weight
##        path[edge] = min_node
##
##    return visited, path



def RandomGraphGenerator(num, ed = 0):
    G = Graph()
    ncr = nCr(num, 2)
    print ncr
    if ed == 0:
        edge = num - 1
    elif ed > ncr:
        edge = ncr
    else:
        edge = ed

    for i in xrange(num):
        G.add_node(chr(ord('a') + i))

    unused = set(G.nodes)
    used = set()

    #for i in xrange(edge):
    #    print len(unused)
    i = 0
    while len(unused)!= 0:

        if i == 0:
            f = rd.sample(unused, 2)
            d = rd.randrange(0, 101)
            G.add_edge(f[0], f[1], d)
            print i, f[0], f[1], d
            unused.remove(f[0])
            unused.remove(f[1])
            used.add(f[0])
            used.add(f[1])
        else:
            f = rd.sample(used, 1)
            g = rd.sample(unused, 1)
            d = rd.randrange(0, 101)
            print i, f[0], g[0], d
            G.add_edge(f[0], g[0], d)
            unused.remove(g[0])
            used.add(g[0])
        i = i + 1

    while i < edge:
        g = rd.sample(used, 2)
        if not ((g[0], g[1]) in G.distances):
            G.add_edge(g[0], g[1], d)
            print i, g[0], g[1], d
            i = i + 1

    print used
    print G.edges
    print G.distances

    return G



def main():
    G = RandomGraphGenerator(5, 100)

    print G.edges
    print G.distances


if __name__ == '__main__':
    main()
