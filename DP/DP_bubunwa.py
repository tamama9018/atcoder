# 部分和問題
# n:個数 k:部分和
n, k = (int(i) for i in input().split())
A = [0] + [int(i) for i in input().split()]
MAX = 10
dp = [[False] * (MAX+1) for i in range(n+1)]
dp[0][0] = True
for i in range(1, n+1):
  for j in range(MAX+1):
    # A[i]を選ぶ場合
    if j >= A[i]:
      if dp[i-1][j-A[i]]:
        dp[i][j] = True
    # A[j]を選ばない場合
    if dp[i-1][j]:
      dp[i][j] = True
print(dp[n][k])
