#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    tree = dict()
    nodeId = 0
    tree[0] = {}
    for p in patterns:
        currNode = tree[0]

        for i in range(len(p)):

            currNodeId = 0
            if not p[i] in currNode:
                nodeId += 1
                currNode[p[i]] = nodeId
                if nodeId in tree:
                    currNode = tree[nodeId]
                else:
                    tree[nodeId] = {}
                    currNode = tree[nodeId]
            else:
                currNodeId = currNode[p[i]]
                currNode = tree[currNodeId]

    return tree


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    patterns = []
    for i in range(n):
        patterns.append(sys.stdin.readline().strip())


    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
