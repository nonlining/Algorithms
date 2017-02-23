# python2

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(raw_input().strip())
                self.parent = map(int, raw_input().strip().split(' '))

        def compute_height(self):
                # Replace this code with a faster implementation
                maxHeight = 0
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        while i != -1:
                                height += 1
                                i = self.parent[i]
                        maxHeight = max(maxHeight, height);
                return maxHeight;

class TreeNode:
    def __init__(self, id = 0):
        self.child = []
        self.id = id
    def addChild(self, node):
        self.child.append(node)

class Tree:
    def __init__(self):
        self.root = None
        self.n = 0
    def construct(self):
        self.n = int(raw_input().strip())
        self.parent = map(int, raw_input().strip().split(' '))
        Nodes = map(lambda x: TreeNode(x) ,range(self.n))

        for i in range(self.n):
            if self.parent[i] == -1:
                self.root = Nodes[i]
            else:
                Nodes[self.parent[i]].addChild(Nodes[i])

    def height(self, TreeNode):
        if TreeNode == None:
            return 0
        m = 0
        #print TreeNode.child
        for i in TreeNode.child:
            m = max(m, self.height(i))
        return m + 1



def main():
  #tree = TreeHeight()
  #tree.read()
  #print(tree.compute_height())
  tree = Tree()
  tree.construct()
  print tree.height(tree.root)


threading.Thread(target=main).start()
