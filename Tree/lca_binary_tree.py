class Node:

    def __init__(self, key):
        self.key = key
        self.children = []


def findLCAUtil(root, nodes, v):

    if root is None:
        return None

    if root.key in nodes :
        v[nodes.index(root.key)] = True
        return root

    if root.key in nodes:
        v[nodes.index(root.key)] = True
        return root
    n = 0
    roots = []
    for i in range(len(root.children)):
        r = findLCAUtil(root.children[i], nodes, v)
        roots.append(r)
        n += 1 if r else 0


    if n == len(v):
        return root

    for r in roots:
        if r is not Node:
            return r


def find(root, k):


    if root is None:
        return False

    if root.key == k:
        return True

    for i in root.children:
        if find(i, k):
            return True

    return False


def findLCA(root, nodes):

    v = [False] * len(nodes)
    lca = findLCAUtil(root, nodes, v)

    n = 0
    for i in v:
        if i is True:
            n += 1

    for i in range(len(v)):
        if v[i] is False:
            if(find(lca, nodes[i])):
                n += 1

    if n == len(nodes):
        return lca
    else:
        return None



def main():
    root = Node(1)
    root.children = [Node(2), Node(3)]

    root.children[0].children = [Node(4), Node(5)]

    root.children[1].children = [Node(6), Node(7)]


    lca = findLCA(root, [4, 5])

    if lca is not None:
        print "LCA(4, 5) = ", lca.key
    else :
        print "Keys are not present"

    lca = findLCA(root, [4, 2])
    if lca is not None:
        print "LCA(4,2) = ", lca.key
    else:
        print "Keys are not present"

    lca = findLCA(root, [6, 2])
    if lca is not None:
        print "LCA(6,2) = ", lca.key
    else:
        print "Keys are not present"

    lca = findLCA(root, [5, 10])
    if lca is not None:
        print "LCA(5,10) = ", lca.key
    else:
        print "Keys are not present"

if __name__ == "__main__":
    main()

