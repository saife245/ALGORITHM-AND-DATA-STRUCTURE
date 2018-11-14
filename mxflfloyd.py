#md saif uddin
#Roll - CSE/16018
#Reg - 000175


from collections import defaultdict 

class Graph: 
   
    def __init__(self,graph): 
        self.graph = graph
        self. no_rows = len(graph)  
    
    def BFS(self,s, t, parent): 

        visited =[False]*(self.no_rows) 
        queue=[] 
        queue.append(s) 
        visited[s] = True

        while queue: 
            u = queue.pop(0) 
            for ind, val in enumerate(self.graph[u]): 
                if visited[ind] == False and val > 0 : 
                    queue.append(ind) 
                    visited[ind] = True
                    parent[ind] = u 
        return True if visited[t] else False

    def FordFulkerson(self, source, sink): 
        parent = [-1]*(self.no_rows) 
  
        max_flow = 0
        while self.BFS(source, sink, parent) : 
            path_flow = float("Inf") 
            s = sink 
            while(s !=  source): 
                path_flow = min (path_flow, self.graph[parent[s]][s]) 
                s = parent[s] 

            max_flow +=  path_flow 

            v = sink 
            while(v !=  source): 
                u = parent[v] 
                self.graph[u][v] -= path_flow 
                self.graph[v][u] += path_flow 
                v = parent[v] 
  
        return max_flow 
  
  
graph = [[0, 3, 0, 5, 0, 2, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 2, 0, 0, 3],
        [0, 0, 0, 0, 4, 3, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 2, 2, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0]] 
  
g = Graph(graph) 
  
source = 0; sink = 7
   
print ("The maximum possible flow is %d " % g.FordFulkerson(source, sink))
