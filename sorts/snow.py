'''
Task: We get an array with n tiles. On every tile there is x snow.
      We can take snow from either side.
      If you don't take snow from the edge every tile before the selected one will be run over.
      You can take 1 pile per day and after each day every pile melts by 1.
      What is the maximum amount of snow that can be collected?
'''



'''Armatys Konrad 415566
Algorytm: chcemy zebrać num największych górek gdzienumjest większe od ilości śniegu w num+1 (posortowane po ilośći śniegu malejąco);
            bez względu na to jakie górki i w jakiej kolejnośći weżmiemy stopnieje tyle samo śniegu;
            na początku zauważmy że bierzemy wszystkie górki które mają więcej bądź równo niż n śniegu bo one i tak się nie stopią;
            następnie pozostają Nam górki z zakresu od 0 do n-1 i na nich wykonujemy counting sorta;
            po tem przechodzimy po posortowanej tablicy tak długa jak będzie zachodzić warunek z num.
Złożoność: O(n)'''


def snow( S ):
    sum = 0
    
    ln = len(S)
    T = [0 for _ in range(ln)]
    
    num = 0
    for val in S:
        if val >= ln:
            num+=1
            sum+=val
        else:
            T[val]+=1
    
    
    j = ln-1
    while num < j:
        if T[j]:
            num+=1
            sum+=j
            T[j]-=1
        else:
            j-=1
            
    return sum - num*(num-1)/2


S = [1, 7, 3, 4, 1]
#print(snow(S))
