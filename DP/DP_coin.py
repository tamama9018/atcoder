n = int(input())
P = [0] + [float(i) for i in input().split()]
# dp[i][j] = i枚目のコインまで投げた時、表がj枚出る確率
dp = [[0] * (n+1) for i in range(n+1)]
dp[1][0] = 1 - P[1]
dp[1][1] = P[1]
for i in range(2, n+1):
  for j in range(i+1):
    # i-1枚まで表j-1枚、i枚目で表 or
    # i-t枚まで表j枚、 i枚目で裏  
    if j > 0:
      dp[i][j] = dp[i-1][j-1] * P[i] + dp[i-1][j] * (1-P[i])
    else:
      dp[i][j] = dp[i-1][j] * (1 - P[i])
ans = 0
for j in range(n+1):
  if j > n-j:
    ans += dp[n][j]
print(ans)
