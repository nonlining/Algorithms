# python3
import sys

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

def reConstruct(tree, node, text, result):
    if (len(tree[node]) == 1):
        for n in tree[node]:
            text = text + n
            reConstruct(tree, tree[node][n], text, result)
    elif (len(tree[node]) > 1):
        for n in tree[node]:
            if (len(tree[tree[node][n]]) > 1):
                result.append(n)
                text = ""
            else:
                text = n
            reConstruct(tree, tree[node][n], text, result)
    else:
        result.append(text)
        text = ""




def build_suffix_tree(text):
    t = []
    for i in range(len(text)):
        t.append(text[i:])

    tree = build_trie(t)
    print tree

    result = []

    reConstruct(tree, 0, "", result)

    return result


if __name__ == '__main__':
  #text = sys.stdin.readline().strip()
  text = "ACACAA$"

  result = build_suffix_tree(text)
  print("\n".join(result))