from egz1btesty import runtests # 11:34

'''Armatys Konrad 415566
Algorytm: dla każzdej planety trzymamy najmniejszą cenę aby dotrzeć do niej z E0(od 0 do E) paliwa
        gdy będziemy mieli dane dla pewnej planety(p) to sprawdzamy gdzie można się z niej teleportować
        przy paliwie równym 0 i tam ustawiamy nowy koszt(nie można się teleportować do przodu więc nie nadpiszemy wcześniej odwiedzonych planet),
        następnie rozważamy nową planetę(p+1) i odejmując ilość paliwa potrzebną do przelotu (z poprzedniej na aktualną planetę) obliczamy najtańsza cenę dotarcia na tę planetę z 0 paliwa
        wiemy że dla t paliwa optymalne jest albo zatankować 1 litr więcej na tej planecie albo przyejchać z 1 litrem paliwa więcej na start(chyba że bak na to nie pozwala)
        za każdym razem mamy optymalne rozwiązanie dla x-1 planety i na podstawie tego obliczamy poprawne rozw dla planety x
Złożoność: O(nE)
'''


def planets( D, C, T, E ):
    ln = len(D)
    dp = [[float('inf') for _ in range(ln)] for __ in range(E +1)]
    
    
    for i in range(E+1):
        dp[i][0] = i * C[0]
    
    dp[0][T[0][0]] = T[0][1]
    
    
    for i in range(1, ln):
        
        dist = D[i] - D[i -1]
        dp[0][i] = min(dp[0][i], dp[dist][i -1]) #przelot na aktualną planetę po któym zosatje pusty bak
        
        for j in range(1, E +1): #dotankowanie 1 paliwa na aktualnej planecie
            dp[j][i] = min(dp[j][i], dp[j -1][i] + C[i])
            
            if j + dist <= E: #sprawdzanie możliwej pojemności baku
                dp[j][i] = min(dp[j][i], dp[j + dist][i -1])
    
    
        if T[i][0] > i:
            dp[0][T[i][0]] = min(dp[0][T[i][0]], dp[0][i] + T[i][1]) #rozważanie teleportacji
        
        
    return dp[0][ln -1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )