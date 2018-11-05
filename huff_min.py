import time

class MinHeap():
  def __init__(self):
    self.heap = []

  def heapify(self, cRoot):
    size = self.length()

    SmIdx = cRoot
    LCIdx = 2 * cRoot + 1
    RCIdx = 2 * cRoot + 2

    if (LCIdx < size and self.heap[cRoot][0] > self.heap[LCIdx][0]):
      SmIdx = LCIdx

    if (RCIdx < size and self.heap[cRoot][0] > self.heap[RCIdx][0]):
      SmIdx = RCIdx

    if SmIdx != cRoot:
      self.heap[SmIdx], self.heap[cRoot] = self.heap[cRoot], self.heap[SmIdx]
      self.heapify(SmIdx)


  def insert(self, element):
    self.heap.append(element)

    size = self.length()
    for i in range(size-1, -1, -1):
      self.heapify(i)

  def extractMin(self):
    temp = self.heap.pop(0)

    size = self.length()
    for i in range(size-1, -1, -1):
      self.heapify(i)

    return temp

  def length(self):
    return len(self.heap)

class heap_node_stucture(object):
  def __init__(self, left=None, right=None):
    self.left = left
    self.right = right


def getFrequency():
  file = open('sample.txt')
  text = file.read()
  text = text.rstrip()

  freqDict = {}
  for character in text:
    if not character in freqDict:
      freqDict[character] = 0
    freqDict[character] += 1
  file.close()

  frequency = []

  for key in freqDict.keys():
    frequency.append((freqDict[key], key))

  return frequency

freq = getFrequency()


def form_heap(frequencies):
    heap = MinHeap()
    for value in frequencies:
        heap.insert(value)
    while heap.length() > 1:
        l, r = heap.extractMin(), heap.extractMin()
        node = heap_node_stucture(l, r)
        heap.insert((l[0]+r[0], node))
    return heap.extractMin()


def encode(node, C_code="", code={}):
    if isinstance(node[1].left[1], heap_node_stucture):
        encode(node[1].left,C_code+"0", code)
    else:
        code[node[1].left[1]]=C_code+"0"
    if isinstance(node[1].right[1],heap_node_stucture):
        encode(node[1].right,C_code+"1", code)
    else:
        code[node[1].right[1]]=C_code+"1"
    return(code)

startTime = time.time()

node = form_heap(freq)
code = encode(node)

endTime = time.time()

for i in sorted(freq, reverse=True):
    print(i[1], '{}'.format(i[0]), code[i[1]])

print ('Time taken {}'.format(endTime - startTime))





