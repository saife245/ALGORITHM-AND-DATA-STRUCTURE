class Heap(object):
    HEAP_SIZE = 10

    def __init__(self):
        self.heap = [0]*Heap.HEAP_SIZE
        self.currentPosition = -1

    def insert(self, item):
        if self.isFull():
            print ('HEAP IS FULL')
            return

        self.currnetPosition = self.currentPosition + 1
        self.heap[self.currentPosition] = item
        self.fixUp(self.currentPosition)

    def fixUp(self, index):
        parentIndex = int((index-1)/2)
        #checking whether the heap property is violeted or, not
        while parentIndex >= 0 and self.heap[parentIndex]< self.heap[index]:
            temp = self.heap[index]
            self.heap[index]=self.heap[parentIndex]
            self.heap[parentIndex]=temp
            parentIndex = (int)((index-1)/2)

    def heapsort(self):
        for i in range(0, self.currentPosition + 1):
            temp = self.heap[0]
            print("{}" .format(temp))
            self.heap[0] = self.heap[self.currentPosition - i]
            self.heap[self.currentPostion - i] = temp
            self.fixDown(0, self.currentPosition - i - 1)
            
    def fixDown(self, index, upto):
        while index <= upto:

            leftChild = 2*index + 1
            rightChild = 2*index + 2

            if leftChild < upto:
                childToSwap = None

                if rightChild > upto:
                    childToSwap = leftChild
                else:
                    if self.heap[leftChild] > self.heap[rightChild]:
                        childToSwap = leftChild
                    else:
                        childToSwap = rightChild

                if self.heap[index] < self.heap[childToSwap]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[childToSwap]
                    self.heap[childToSwap] = temp

                else:
                    break

                index = childToSwap

            else:
                break
            
    def isFull(self):
        if self.currentPosition == Heap.HEAP_SIZE:
            return True
        else:
            return False
        

if __name__ == "__main__":
    heap = Heap()

    heap.insert(10)
    heap.insert(20)
    heap.insert(30)
    heap.insert(40)
    heap.insert(50)
    heap.heapsort()

