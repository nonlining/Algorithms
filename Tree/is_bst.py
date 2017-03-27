#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def isBST(tree, rootIndex,lower, upper):
    if (rootIndex == -1):
        return True
    root = tree[rootIndex]

    left = isBST(tree, root[1], lower, root[0])
    right = isBST(tree, root[2], root[0], upper)
    return root[0] > lower and root[0] < upper and left and right

def IsBinarySearchTree(tree):

    if len(tree) == 0 or tree == None:
        return True
    return isBST(tree, 0, float('-inf'), float('inf'))


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
