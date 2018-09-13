class Node(object):
    #calling the constructer
    def __init__(self, name):
        self.name = name
        self.adjacencyList = []
        self.visited = False
        self.predecessor = None

class BFS(object):
    def bfs(self, startNode):

        #in bfs we use queue
        queue = []
        queue.append(startNode)
        startNode.visited = True

        while queue:#run until queue is empty
            actualNode = queue.pop(0)
            print("{}".format(actualNode.name))

            for n in actualNode.adjacencyList:
                if not n.visited:
                    n.visited = True
                    queue.append(n)

node1 = Node('a')
node2 = Node('b')
node3 = Node('c')
node4 = Node('d')
node5 = Node('e')

node1.adjacencyList.append(node2)
node1.adjacencyList.append(node3)
node2.adjacencyList.append(node4)
node4.adjacencyList.append(node5)

bfs = BFS()
bfs.bfs(node1)
