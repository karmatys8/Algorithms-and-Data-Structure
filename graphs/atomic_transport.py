'''
Task: We get the graph (G) and two starting locations s and t.
      We have to transport atomic substances whilst keeping them at least min_d distance between them.
      Our task is to determine whether it is possible to make atomic substances swap places.
      s -> t and t -> s keeping min_d at all time
'''



def atomic_transport(G, s, t, min_d):
    ln = len(G)
    
    inf = float('inf')
    dist_G = [[inf for _ in range(ln)] for __ in range(ln)]
    
    for i in range(ln):
        dist_G[i][i] = 0
    
    for u in range(ln):
        for v, val in G[u]:
            dist_G[u][v] = val
            dist_G[v][u] = val
            
    for i in range(ln):
        for j in range(ln):
            for k in range(ln):
                dist_G[j][k] = min(dist_G[j][k], dist_G[j][i] + dist_G[i][k])
            
    
    incidents_G = [[] for _ in range(ln*ln)]
    
    for u in range(ln):
        for v in range(ln):
            if dist_G[u][v] >= min_d:
                for vector, val in G[u]:
                    if dist_G[vector][v] >= min_d:
                        incidents_G[v*ln + vector].append(v*ln + u)
                        incidents_G[u*ln + v].append(vector*ln + v)
                        
                
    visited = [False for _ in range(ln*ln)]
    parents = [None for _ in range(ln*ln)]
    
    def dfs_visit(G, u):
        visited[u] = True
        
        for v in G[u]:
            if not visited[v]:
                parents[v] = u
                
                dfs_visit(G, v)
                
    dfs_visit(incidents_G, s*ln + t)
    
    
    return visited[t*ln + s]


G = [[(1, 1), (2, 12)],
     [(0, 1), (2, 8), (4, 2)],
     [(0, 12), (1, 8), (3, 11)],
     [(2, 11), (4, 7), (5, 2)],
     [(1, 2), (3, 7), (5, 1)],
     [(3, 2), (4, 1)]]
print(atomic_transport(G, 0, 5, 4))
