# python2

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(raw_input())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]

    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())

      self.key[i] = a
      self.left[i] = b
      self.right[i] = c


  def inOrderRecur(self, root , result):
    if (root == -1):
        return
    self.inOrderRecur(self.left[root], result)
    result.append(self.key[root])
    self.inOrderRecur(self.right[root], result)

  def preOrderRecur(self, root , result):
    if (root == -1):
        return
    result.append(self.key[root])
    self.preOrderRecur(self.left[root], result)
    self.preOrderRecur(self.right[root], result)

  def postOrderRecur(self, root , result):
    if (root == -1):
        return
    self.postOrderRecur(self.left[root], result)
    self.postOrderRecur(self.right[root], result)
    result.append(self.key[root])

  def inOrder(self):
    self.result = []
    self.inOrderRecur(0, self.result)

    return self.result

  def preOrder(self):
    self.result = []
    self.result = []
    self.preOrderRecur(0, self.result)

    return self.result

  def postOrder(self):
    self.result = []
    self.postOrderRecur(0, self.result)

    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
