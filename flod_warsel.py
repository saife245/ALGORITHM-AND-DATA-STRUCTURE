INF = float("inf")
NIL = "NIL"
V = 5
 
def floyd(graph):   
    for k in range(V):
        for i in range(V):
            for j in range(V):

                if dist[i][k]+ dist[k][j] <dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[k][j]

    print("Distance matrix\n")
    print_func_dist(dist)
    print("Path matrix\n")
    print_func_path(path)
 
 

def print_func_dist(dist):
    for i in range(V):
        for j in range(V):
            if(dist[i][j] == INF):
                print("\tINF"),
            else:
                print("\t"+str((dist[i][j]))),
            if j == V-1:
                print("\n")

def print_func_path(path):
    for i in range(V):
        for j in range(V):
            if(i ==j):
                print("\tNIL"),
            else:
                print("\t"+str((path[i][j]+1))),
        print("\n")

graph = []

dist = [[INF for x in range(V)] for y in range(V)]
path = [[NIL for x in range(V)] for y in range(V)] 

for i in range(V):
    for j in range(V):
        if i == j :
            dist[i][j] = 0


[graph.append(tuple(int(i) for i in t.strip('()').split(','))) for t in open('input.txt').read().split()]


for ele in graph:
    dist[ele[0]][ele[1]] = ele[2]
    path[ele[0]][ele[1]] = ele[0]


floyd(graph)