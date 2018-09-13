class Node(object):

    def __init__(self, name):
        self.name = name
        self.adjacencyList = []
        self.visited = False
        self.predecessor = None

class DFS(object):

    def dfs(self, node):
        node.visited = True
        print("{}".format(node.name))

        # we can traverse either right or left it doesn't matter
        for n in node.adjacencyList:
            if not n.visited:
                self.dfs(n)

node1 = Node('a')
node2 = Node('b')
node3 = Node('c')
node4 = Node('d')
node5 = Node('e')

node1.adjacencyList.append(node2)
node1.adjacencyList.append(node3)
node2.adjacencyList.append(node4)
node4.adjacencyList.append(node5)

dfs = DFS()
dfs.dfs(node1)
