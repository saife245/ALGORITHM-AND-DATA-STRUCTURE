class Graph: 
    def __init__(self,graph): 
        self.graph = graph  
        self.ppl = len(graph) 
        self.jobs = len(graph[0]) 

    def BP_Match(self, u, match, seen): 
        for v in range(self.jobs): 

            if self.graph[u][v] and seen[v] == False: 

                seen[v] = True 
                if match[v] == -1 or self.BP_Match(match[v], match, seen): 
                    match[v] = u 
                    return True
        return False

    def Max_Bipartite(self): 
        match = [-1] * self.jobs 

        result = 0 
        for i in range(self.ppl): 
            seen = [False] * self.jobs 
            if self.BP_Match(i, match, seen): 
                result += 1
        return result 


bpg =[[1, 1, 0, 0, 0],
      [1, 0, 0, 0, 0],
      [0, 1, 1, 0, 0],
      [0, 0, 1, 1, 1],
      [0, 0, 0, 0, 1]
      ] 
  
g = Graph(bpg) 

print("Maximum matching is:")
print (g.Max_Bipartite()) 