from egz1Atesty import runtests #12:18
from queue import PriorityQueue

'''Armatys Konrad 415566
Algorytm: na początku obliczamy odległość z s do każdego miasta zakładając że nie kradniemy;
          następnie obliczamy odległość z t do każdego miasta zakładając że już ukradliśmy;
          na start zakładamy że najkrótsza droga to taka w której nic nie kradniemy --XX
          na koniec przechodzimy po każdym mieście i bierzemy min z {droga z s + drogi do t - sztabki w skarbcu} --YY
          wynikiem jest min(XX, YY)
Złożoność: O(E * logV) <= O(V^2 * logV)
'''

def gold(G,V,s,t,r):
  ln = len(G)
  
  dist_s = [float('inf') for _ in range(ln)] #obliczanie dystansu z s bez kradnięcia przy pomocy dijkstry
  dist_s[s] = 0
  
  pro_que = PriorityQueue()
  pro_que.put((0, s))
  
  while not pro_que.empty():
    cost, u = pro_que.get()
    
    for v, val in G[u]:
      if dist_s[v] > cost + val:
        dist_s[v] = cost + val
        
        pro_que.put((dist_s[v], v))
  
  
  dist_t = [float('inf') for _ in range(ln)] #obliczanie dystansu do t po ukradnięciu za pomocą dijkstry
  dist_t[t] = 0
  
  pro_que = PriorityQueue()
  pro_que.put((0, t))
  
  while not pro_que.empty():
    cost, u = pro_que.get()
    
    for v, val in G[u]:
      if dist_t[v] > cost + 2*val +r:
        dist_t[v] = cost + 2*val +r
        
        pro_que.put((dist_t[v], v))
  
  
  
  curr_min = dist_s[t] #obliczanie wyniku końcowego
  for i in range(ln):
    curr_min = min(curr_min, dist_s[i] + dist_t[i] - V[i])
  
  
  return curr_min

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )