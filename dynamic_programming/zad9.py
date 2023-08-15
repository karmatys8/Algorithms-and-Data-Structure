from zad9testy import runtests
from queue import PriorityQueue

''' Armatys Konrad 415566
Algorytm: na początku nie przejmójemy się 2 warunkiem i zapisujemy cenę najtańszej trasy z każdego parkingu do A i B;
            wyznaczamy je idąc od danego miasta(rozważmy miasto A) i idąc od najbliższego miasta x,
            patrzymy wtedy T do tyłu i szukamy najmniejszej ceny i odajemy od niej cenę postoju w mieśce x;
            czynność powtarzamy aż nie będziemy mieli wszystkich wart. dla miasta A i potem dla miasta B; *
            potem próbujemy przejechać z każdego pola o 2T i szukamy najmniejszej wart takiej trasy korzystając z faktu że:
            przed i po wykonaniu przejazdu 2T chcemy jechać najtańszymi trasami o dł. nie większej od T (czyli korzystamy z teg co wcześniej obliczyliśmy);
            bierzemy najmniejszą z wart. łącznej trasy z wykorzystaniem przejazdu 2T.
            
            * wiemy że znalezione trasy będą najkrótsze bo możemy jechać max, T, więc patrząc T do tyłu rozważamy wszytskie miasta z których może wieść optymalna trasa
            i wiemy że te wart. zostały obliczone wcześniej i są poprawne;
Złożoność: O(n*log(n)) - sortowanie i n razy wyciąganie elem. z kolejki (n*log(n))
'''

def min_cost( O, C, T, L ):
    inf = float('inf')
    ln = len(O) +2
    
    P = [(O[i], C[i]) for i in range(len(O))]
    P.append((0, 0))
    P.sort()
    P.append((L, 0))
    
    cost_a = [inf for _ in range(ln)]
    pro_que_a = PriorityQueue()
    cost_a[0] = 0

    min_val = (cost_a[0], 0)
    for i in range(1, ln):
        while P[i][0] > min_val[1] +T  and  not pro_que_a.empty():
            min_val = pro_que_a.get()
            
        
        cost_a[i] = min_val[0] + P[i][1]
        pro_que_a.put((cost_a[i], P[i][0]))
     
    
    
    cost_b = [inf for _ in range(ln)]
    pro_que_b = PriorityQueue()
    cost_b[ln -1] = 0

    min_val = (cost_b[ln -1], L)
    for i in range(ln -2, -1, -1):
        while P[i][0] <= min_val[1] -T -1  and  not pro_que_b.empty():
            min_val = pro_que_b.get()
            
        
        cost_b[i] = min_val[0] + P[i][1]
        pro_que_b.put((cost_b[i], P[i][0]))
    
        
    
    res = inf
    res_que = PriorityQueue()
    
    min_val = (0, 0)   
    for i in range(1, ln):
        while P[i][0] > min_val[1] +2*T  and  not res_que.empty():
            min_val = res_que.get()
            
        
        res = min(res, (min_val[1] + 2*T < L) * cost_b[i] + min_val[0])
        res_que.put((cost_a[i], P[i][0]))
    
    
    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )