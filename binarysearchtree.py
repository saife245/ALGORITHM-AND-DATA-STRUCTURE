class Node(object):

    def __init__(self, data):  #CALLING THE CONSTRUCTER
        self.data = data  #storing the data
        self.leftChild = None
        self.rightChild = None


class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)

    def insertNode(self, data, node):
        #if data is smaller than root we have to choose left sub tree
        if data < node.data:
            if node.leftChild:# if there is node present the we call recurrsively
                self.insertNode(data, node.leftChild) #calling function recrrsively
            else:  #if not present any node we directly insert data by calling the Node function
                node.leftChild = Node(data)
         #and if data is greater than root node then we have to choose right sub tree
        else:
            if node.rightChild:# again we check for right subtree
                self.insertNode(data, node.rightChild)
            else:
                node.rightChild = Node(data)

    def removeNode(self, data, node):
        if not node:
            return node

        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)
        else:
            if not node.leftChild and not node.rightChild:
                print("removing the leaf node")
                del node
                return None

            if not node.leftChild:
                print("remove a node with single right child")
                tempNode = node.rightChild
                del node
                return tempNode

            elif not node.rightChild:
                print("removing node with singl node")
                tempNode = node.leftChild
                del Node
                return tempNode

            print("removing node with two child")
            tempNode = self.getPredecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)
        return node
        
    def getPredecessor(self, node):
        if node.rightChild:
            return self.getPredecessor(node.rightChild)
        return node

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)
            
    def getMinValue(self):
        if self.root:     #if it has root then we go to the left child
            return self.getMin(self.root)

    def getMin(self, node):
        if node.leftChild:
            return self.getMin(node.leftChild) #called recurrcively o find minimum

        return node.data

    def getMaxValue(self):
        if self.root:     #if it has root then find max in right child
            return self.getMax(self.root)

    def getMax(self, node):
        if node.rightChild:
            return self.getMax(node.rightChild)

        return node.data

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self,node):

        if node.leftChild:
            self.traverseInOrder(node.leftChild)

        print("{}" .format( node.data))

        if node.rightChild:
            self.traverseInOrder(node.rightChild)

bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(18)
bst.insert(2)

print(bst.getMinValue())
print(bst.getMaxValue())
bst.traverse()
bst.remove(2)
