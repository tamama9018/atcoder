w = int(input())
n, k = (int(i) for i in input().split())
dp = [[[0]*(w+1) for i in range(k+1)] for i in range(n+1)]
for i in range(1, n+1):
  # a:幅 b:重要度
  a, b = (int(i) for i in input().split())
  for h in range(1, k+1):
    for j in range(w+1):
      if j-a >= 0:
        dp[i][h][j] = max(dp[i-1][h][j],
                          dp[i-1][h-1][j-a] + b)
      else:
        dp[i][h][j] = dp[i-1][h][j]
      
print(dp[n][k][w])
