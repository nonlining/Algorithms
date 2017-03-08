# python2

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(raw_input())
    self._data = [int(s) for s in raw_input().split(' ')]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print swap[0], swap[1]

  def ShiftDown(self, index):

    if 2*index + 1 >= len(self._data):
        return

    minIndex = index

    leftNode = self._data[2*index + 1]

    if leftNode < self._data[minIndex]:
        minIndex = 2*index + 1

    if (2*index + 2) < len(self._data) and self._data[2*index + 2] < self._data[minIndex]:
        minIndex = 2*index + 2
    if (index != minIndex):
        self._swaps.append((index, minIndex))
        self._data[index], self._data[minIndex] = self._data[minIndex], self._data[index]
        self.ShiftDown(minIndex)


  def GenerateSwaps(self):
    n = len(self._data)
    for i in range(n/2, -1, -1):
        self.ShiftDown(i)

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
