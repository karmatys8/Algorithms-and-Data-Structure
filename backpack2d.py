def backpack2d(T, w, h):
  ln = len(T)
  
  dp = [[0 for _ in range(h +1)] for __ in range(w +1)]
  
  for i in range(T[0][1], w +1):
    for j in range(T[0][2], h +1):
      dp[i][j] = T[0][0]
      
  for i in range(1, ln):
    for j in range(w, T[i][1] -1, -1):
      for k in range(h, T[i][2] -1, -1):
        dp[j][k] = max(dp[j - T[i][1]][k - T[i][2]] + T[i][0], dp[j][k])
        
  return dp[w][h]


T = [(4, 1, 0), (20, 5, 3), (13, 6, 2), (1, 0, 1), (5, 2, 0), (100000, 11, 0), (1000000, 0, 4), (99, 9, 3)]
w = 10
h = 3

print(backpack2d(T, w, h))