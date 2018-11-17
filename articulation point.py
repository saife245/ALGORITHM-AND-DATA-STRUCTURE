from collections import defaultdict
result = defaultdict(list)

Art = []
time = 0
path  = []
flag = 0

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
 
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
 
    def DFS_trav(self,u):
        child = 0
        global time
        time = time +1
        low[u] = time
        discovered[u] = time
        color[u] = "G"
        path.append(u)

        for v in self.graph[u]:
            if color[v] == "W":
                child+=1
                parent[v] = u
                self.DFS_trav(v)
                low[u] = min(low[u], low[v])

                if parent[u] == -1 and child >1:
                    Art.append(u)
                
                elif parent[u] != -1 and low[v] >= discovered[u]:
                    Art.append(u)
            
            elif v!=parent[u]:
                low[u] = min(low[u], discovered[v])
                global flag
                flag = 1

        color[u] = "B"
        time += 1
        finish[u] = time
 
    def DFS(self):
        for u in self.graph:
            color[u] = "W"
    

        for u in self.graph:
            if color[u] == "W":
                self.DFS_trav(u)


g = Graph()
# g.addEdge(1,2)
# g.addEdge(1,3)
# g.addEdge(1,4)
# g.addEdge(2,3)
# g.addEdge(2,5)
# g.addEdge(2,6)
# g.addEdge(3,6)
# g.addEdge(4,7)
# g.addEdge(4,8)
# g.addEdge(5,6)
# g.addEdge(7,8)

g.addEdge(6, 3)
g.addEdge(6, 1)
g.addEdge(5, 1)
g.addEdge(5, 2)
g.addEdge(3, 4)
g.addEdge(4, 2)

size = len(g.graph) + 1

discovered = [float("inf")]*size
finish = [0]*size
color = [0] * size
parent = [-1]*size
low = [float("inf")]*size

g.DFS()

print("DFS traveral is :")
print(path)
print("Articulation points are:")
print(Art)

if flag == 1:
    print("Cycle Present")
else:
    print("Cycle Not Present")