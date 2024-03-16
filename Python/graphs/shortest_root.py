'''
Task: Given a tree, find the vertice for which tree rooted in it has the shallowest depth.
'''



def shortest_root(G):
    ln = len(G)
    min_v = (float('inf'), None)
    
    for i in range(ln):
        dist = [float('inf') for _ in range(ln)]
        visited = [False for _ in range(ln)]
        
        def dfs_visit(G, u):
            visited[u] = True
            
            for v, val in G[u]:
                if not visited[v]:
                    dist[v] = dist[u] + val
                    dfs_visit(G, v)
        
        dist[i] = 0    
        dfs_visit(G, i)
           
            
        curr_max = 0
        for val in dist:
            if val > curr_max:
                curr_max = val
                
        if curr_max < min_v[0]:
            min_v = (curr_max, i)
            
    return min_v[1]


G = [[(1, 5)],
     [(0, 5), (2, 3)],
     [(1, 3), (3, 8)],
     [(2, 8), (4, 90)],
     [(3, 90)]]
print(shortest_root(G))
