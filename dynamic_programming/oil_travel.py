from zad8testy import runtests

'''Armatys Konrad 415566
Algorytm: na początku obliczamy ile ropy możemy pobrać z każdego pola na trasie pamiętając że niektóre mogą się łączyć,
            jednak to Nas nie obchodzi bo bez względu na to a w którym miejscu pobierzemy ropę sumarycznie bedzie jej tyle samo i zaliczymy i tak 1 postój,
            więc logicznie byłoby rozważać branie takiej ropy jak najwcześniej żeby mieć do niej najłatwiejszy dostęp;
            pobieramy ropę z pierwszego pola(zaznaczamy że zostało 0 ropy) potem wiemy że na pewno chcemy mieć pobrane największą wart. z aktualnie dostepnych pól(a) i zaznaczamy że źródło już jest puste;
            wiemy że zawsze chcemy wybrać kolejną najwiekszą wartość(b) w zasięgu paliwa, nie musi ona być po poprzednio wybranym miejscu gdyż możemy najpierw zatrzmać się na na 'b' a dopiero potem na 'a',
            powtarzamy czynność aż nie wystarczy Nam paliwa na cały przejazd
            
Złożoność: n*m(zamiana T na tiles) + m^2(znalezienie wyniku) = O(max(n*m, m^2))
'''

def plan(T):
    n = len(T)
    m = len(T[0])
    
    def dfs_visit(x, y):
        nonlocal cnt
         
        cnt += T[x][y]
        T[x][y] = 0
        
        for a, b in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            if 0 <= x+a < n  and  0 <= y+b < m  and  T[x+a][y+b]:
                dfs_visit(x+a, y+b)
    
    
    tiles = [0 for _ in range(m)]
    for i in range(m):
        if T[0][i]:
            cnt = 0
            dfs_visit(0, i)
            
            tiles[i] = cnt


    res = 1
    sum = tiles[0]
    tiles[0] = 0
    
    while sum < m-1:
        max_i = 0
        
        for i in range(sum +1):
            if tiles[i] > tiles[max_i]:
                max_i = i

        sum += tiles[max_i]
        tiles[max_i] = 0
        res+=1
    
    
    return res



runtests( plan, all_tests = True )
