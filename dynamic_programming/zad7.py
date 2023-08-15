from zad7testy import runtests

'''
Armatys Konrad 415566
Algorytm: zauważmy że jeżeli raz pójdziemy w dół to nie możemy już w tej kolumnie iść w górę bo inaczej odwiedzamy jedno pole 2 razy;
            gdy raz wyjdziemy z kolumny nie możemy do niej wrócić i poandto szukamy najdłuższej ścieżki więc w każdej kolumnie szukamy aktualnie najdłuższej ścieżki do danego pkt x;
            może ona być z przejścia bezpośrednio z poprzedniej kolumny albo taka która wędrowała cały czas w dół do naszego x albo cały czas w górę;
            wystarczy w każdej kolumnie przejść z każdego pkt w dół i w górę , jeżeli to możliwe, aktualizując wartość aktualnie najdłuższej ścieżki;
            następnie wybieramy większą z wartości przejścia ścieżką w dół i przejścia ścieżką w górę i przyporzątkowujemy wartość elem. w następnej kolumnie zwiększoną o 1;
            całą czynnośc powtarzamy dla każdej kolumny, przy czm dla krańcowych nie rozważamy ścieżki w górę;
            dodatkowo należy uważać żeby nie stworyć nowego źródła ścieżek poza (0, 0);
Złożoność: O(n^2)
'''

def maze( L ):
    ln = len(L)
    max_dist = [[[0, 0] for __ in range(ln)] for _ in range(ln)]
    if L[0][1] != '#':
        max_dist[0][1][1] = 1
    if L[1][0] != '#':
        max_dist[1][0][1] = 1
    
    for col in range(ln):
        for row in range(1, ln):
            if L[row][col] != '#'  and  max_dist[row -1][col][1]:
                max_dist[row][col][1] = max(max_dist[row][col][1], max_dist[row -1][col][1] +1)
                    
            
        if col != 0  and  col != ln -1:
            for row in range(ln -2, -1, -1):
                if L[row][col] != '#'  and  max_dist[row +1][col][0]:
                    max_dist[row][col][0] = max(max_dist[row][col][0], max_dist[row +1][col][0] +1)
        
             
        if col != ln -1:
            for row in range(ln):        
                if (max_dist[row][col][0]  or  max_dist[row][col][1])  and  L[row][col +1] != '#':
                    curr_max = max(max_dist[row][col][0], max_dist[row][col][1]) +1
                    max_dist[row][col +1][0] = max_dist[row][col +1][1] = curr_max                
         
    
    result = max(max_dist[ln -1][ln -1][0], max_dist[ln -1][ln -1][1])
    return result if result else -1
            


runtests( maze, all_tests = True )