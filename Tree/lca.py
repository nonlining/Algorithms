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

    count = 0
    firstNotNone = None

    for r in roots:
        if r is not None:
            count += 1
            firstNotNone = r

    if count > 1:
        return root
    elif count == 1:
        return firstNotNone
    else:
        return None


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


def test1():
    root = Node(1)
    root.children = [Node(2), Node(3)]

    root.children[0].children = [Node(4), Node(5)]

    root.children[1].children = [Node(6), Node(7)]


    lca = findLCA(root, [4, 5])
    #print lca

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


def test2():
    root = Node(1)
    root.children = map(lambda x: Node(x), range(2, 7))

    root.children[0].children = map(lambda x: Node(x), range(7, 11))

    root.children[3].children = map(lambda x: Node(x), range(11, 14))

    root.children[0].children[0].children = map(lambda x: Node(x), range(14, 16))

    lca = findLCA(root, [2, 7, 9, 6, 11, 13])
    if lca is not None:
        print "LCA(2, 7, 9, 6, 11, 13) = ", lca.key
    else:
        print "LCA(2, 7, 9, 6, 11, 13) Keys are not present"
    lst = [14, 7, 2, 10, 19]
    lca = findLCA(root, lst)

    if lca is not None:
        print "LCA"+str(lst)," = ", lca.key
    else:
        print "LCA"+str(lst)+ " Keys are not present"


if __name__ == "__main__":
    #test1()
    test2()


