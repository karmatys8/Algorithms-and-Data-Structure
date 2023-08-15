from egz1btesty import runtests

'''Armatys Konrad 415566
Algorytm: zauważmy że nasz root zawsze znajdzie się w rozw, załózmy że jest ianczej to wtedy mamy drzewo oszerokości s i wysokości w;
            no ale korzeń naszego wyniku musi być dzieckiem roota więc dla szerokości s możemy osiągnąć wysokośc większą od w;
            najpierw przechodzimy po drzewie i zliczamy ile jest elem na każdej wysokośći,
            potem wybieramy największą z nich, jeżeli jakaś się powiela to bierzemy taką najniżej w drzewie żeby otrzymać największą wysokość;
            w każdym pkt w drzewie czymamy wart. najgłębszeg dziecka;
            potem przechodzimy po drzewie i jeżeli wart. w pkt jest mniejsza od szukanego poziomu lub jesteśmy głebiej niż szukany poziom to odcianmy tę gałąź,
            w przeciwnym przypadku wchodzimy wgłąb;
Złożoność: O(n)
'''

class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None       # pole do wykorzystania przez studentow


def wideentall( T ):
  cnts = [0]
  
  def rek(curr, depth):
    cnts[depth] += 1
    if not curr.left  and  not curr.right:
      curr.x = depth
    else:
      curr.x = depth
      
      depth += 1
      
      if len(cnts) <= depth:
        cnts.append(0)
        
      
      if curr.left:
        rek(curr.left, depth)
        curr.x = curr.left.x
      if curr.right:
        rek(curr.right, depth)
        curr.x = max(curr.x, curr.right.x)
  
  rek(T, 0)
  
  max_i = 0
  for i in range(len(cnts)):
    if cnts[i] >= cnts[max_i]:
      max_i = i
      
  
  res = 0
  def rek_cut(curr, depth, target):
    nonlocal res
    
    if curr.x < target  or  depth > target:
      res += 1
    else:
      depth+=1
      if curr.left:
        rek_cut(curr.left, depth, target)
      if curr.right:
        rek_cut(curr.right, depth, target)
  
  rek_cut(T, 0, max_i)
  
  
  return max_i, cnts[max_i], res


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = True )

A = Node()
B = Node()
C = Node()
A.left = B
A.right = C
D = Node()
E = Node()
B.left = D
B.right = E
F = Node()
E.right = F
G = Node()
F.right = G
#print(wideentall(A))
