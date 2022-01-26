n,w = (int(i) for i in input().split())
W, V = [0], [0]
for i in range(n):
  a, b = (int(i) for i in input().split())
  W.append(a)
  V.append(b)

dp = [[0]*(w+1) for i in range(n+1)]

for i in range(1, n+1):
  for j in range(w+1):
    # max(i番目の荷物を入れない場合, 入れた場合)
    if j >= W[i]:
      dp[i][j] = max(dp[i-1][j],
                   	 dp[i-1][j-W[i]] + V[i])
    else:
      dp[i][j] = dp[i-1][j]
  
print(dp[n][w])
                   
