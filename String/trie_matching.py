# python3
import sys

def build_trie(text):
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

def PrefixTrieMatching(text, trie):
    idx = 0
    s = text[idx]
    currNode = trie[0]


    while True:
        if not currNode:
            return True
        elif s in currNode:
            currNode = trie[currNode[s]]
            idx += 1
            if idx < len(text):
                s = text[idx]
            else:
                s = ""

        else:
            return False


def solve (text, n, patterns):
    trie = build_trie(patterns)
    result = []

    n = len(text)

    for i in range(n):
        if PrefixTrieMatching(text[i:], trie):

            result.append(i)

    return result

if __name__ == '__main__':
   text = sys.stdin.readline().strip()
   n = int (sys.stdin.readline().strip())
   patterns = []
   for i in range (n):
        patterns += [sys.stdin.readline ().strip ()]

   ans = solve(text, n, patterns)

   sys.stdout.write(' '.join (map (str, ans)) + '\n')
