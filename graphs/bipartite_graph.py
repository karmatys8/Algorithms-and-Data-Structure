from zad6testy import runtests
from collections import deque


'''Armatys Konrad 415566
Algorytm:   zbiór pracowników i maszyn są rozłączne więc tworzą graf dwudzielny;
            chcemy aby conajwyżej jeden pracownik pracował na jednej maszynie, czyli z każdego wierzchołka ma wychodzić maksymalnie 1 krawędź;
            rozwiązujemy to za pomocą algorytmu na maksymalne skojarzenia dodając źródło połączone z pracownikami i odpływ do którego połaczone są maszyny;
Złożoność:  n*n(tworzenie listy sąsiedztwa) + n(max ilość wywołań dfs)*[2n + n*n+2*n] = O(n^3)
'''


def bfs(G, s, t):
    ln = len(G)
    
    visited = [False for _ in range(ln)]
    parents = [None for _ in range(ln)]
    
    visited[s] = True
    dqu = deque()
    dqu.append(s)
    
    while len(dqu):
        u = dqu.pop()
        
        if u == t:
            while parents[u] != None:
                v = parents[u]
                
                index = 0
                while G[v][index] != u:
                    index+=1
                    
                G[v].pop(index)
                G[u].append(v)
                
                u = v
            
            return True
        
        
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parents[v] = u
                
                dqu.append(v)
    
                
    return False


def binworker(M):
    ln = len(M)
    G = [[] for _ in range(2*ln +2)]
    
    for w in range(ln):
        for m in M[w]:
            G[w].append(m + ln)
    
    
    s = 2*ln
    t = s + 1
    G[s] = [i for i in range(ln)]
    
    for i in range(ln, s):
        G[i].append(t)
    
    
    flow = 0
    while bfs(G, s, t):
        flow+=1
   
    return flow

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )
