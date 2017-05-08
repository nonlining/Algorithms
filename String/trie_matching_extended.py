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

        currNode['$'] = {}

    return tree

def PrefixTrieMatching(text, trie):
    idx = 0
    s = text[idx]
    currNode = trie[0]

    while True:
        if not currNode: # for trie leaf
            return True
        if '$' in currNode:
            return True # for trie substring
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
    result = set()
    trie = build_trie(patterns)

    n = len(text)
    for i in range(n):
        if(PrefixTrieMatching(text[i:], trie)):
            result.add(i)

    return sorted(list(result))


if __name__ == '__main__':
   text = sys.stdin.readline().strip()
   n = int (sys.stdin.readline().strip())
   patterns = []
   for i in range (n):
        patterns += [sys.stdin.readline ().strip ()]

   ans = solve(text, n, patterns)

   sys.stdout.write(' '.join (map (str, ans)) + '\n')