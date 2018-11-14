#MD SAIF UDDIN
#REG 000175
#ROLL CSE/16018

from collections import defaultdict
result = []

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
 
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    def DFS_trav(self,u):
        color[u] = "G"

        for v in self.graph[u]:
            if color[v] == "W":
                self.DFS_trav(v)
       
        result.insert(0,u)
 
    def DFS(self):
        for u in range(1,size):
            if color[u] == "W":
                self.DFS_trav(u)
                 
    
g = Graph()
g.addEdge(1,2)
g.addEdge(1,8)
g.addEdge(2,3)
g.addEdge(2,8)
g.addEdge(3,6)
g.addEdge(4,3)
g.addEdge(4,5)
g.addEdge(5,6)
g.addEdge(7,8)


size = 9

color = ["W"] * size

g.DFS()
print(result)

