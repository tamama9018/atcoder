n, w = (int(i) for i in input().split())
W, V = [0], [0]
for i in range(n):
  a, b = (int(i) for i in input().split())
  W.append(a)
  V.append(b)
jmax = 10**5
dp = [[float("inf")]*(jmax+1) for i in range(n+1)]
dp[0][0] = 0
for i in range(1, n+1):
  for j in range(jmax+1):
    if j >= V[i]:
      dp[i][j] = min(dp[i-1][j],
                     dp[i-1][j-V[i]] + W[i])
    else:
      dp[i][j] = dp[i-1][j]
# dp[n]を後ろから見てゆき、最初にwが容量以下に
#　なった時のvが答え
for i, weight in enumerate(dp[n][::-1]):
  if weight <= w:
    print(jmax - i)
    exit()


