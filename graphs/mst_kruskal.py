'''
Task: Implement Kruskal's algorithm
algorithm: https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
'''



class Kruskal:
    def __init__(self, G):
        self.n_G = []
        
        for u in range(len(G)): #neighbour list to edge list
            for v, val in G[u]:
                if u > v:
                    self.n_G.append((val, v, u))
                else:
                    break
        
        '''
        ln = len(G)
        for i in range(ln): #matrix to edge list
            for j in range(i+1, ln):
                if G[i][j] != float('inf'):
                    self.n_G.append((G[i][j], i, j))
        '''
        
                
        self.n_G.sort()
        
        self.parents = [i for i in range(len(self.n_G))]
        self.ranks = [0 for _ in range(len(self.n_G))]  
    
    
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
            
        return self.parents[x]


    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        
        x_rank = self.ranks[x_root]
        y_rank = self.ranks[y_root]
        
        if x_rank > y_rank:
            self.parents[y_root] = x_root
        else:
            self.parents[x_root] = y_root
                    
            if x_rank == y_rank:
                self.ranks[y_rank] += 1
                
                
    def mst(self):
        res = []
        
        for edge in self.n_G:
            if self.find(edge[1]) != self.find(edge[2]):
                self.union(edge[1], edge[2])
                
                res.append(edge)
            
                   
        return res
    
    

G = [[(1, 4), (3, 30), (6, 40)],
     [(0, 4), (2, 20)],
     [(1, 20), (5, 3), (6, 5)],
     [(0, 30), (4, 3), (5, 18)],
     [(3, 3), (10, 8), (11, 9)],
     [(2, 3), (3, 18), (6, 6)],
     [(0, 40), (2, 5), (5, 6), (7, 10), (8, 10), (11, 31)],
     [(6, 10), (9, 10), (11, 14)],
     [(6, 10), (10, 18)],
     [(7, 10), (10, 7), (11, 300)],
     [(4, 8), (8, 18), (9, 7)],
     [(4, 9), (6, 31), (7, 14), (9, 300)]]
a = Kruskal(G)
print(a.mst())
