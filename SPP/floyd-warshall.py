N, M = (int(i) for i in input().split())
G = [[float('inf')]*(N+1) for i in range(N+1)]
for i in range(N+1):
  G[i][i] = 0
for i in range(M):
  a, b, c = (int(i) for i in input().split())
  G[a][b] = c
  
def floyd_warshall():
  for k in range(N): # 経由地点
    for i in range(N): # 始点
      for j in range(N): # 終点
        G[i][j] = min(G[i][j], G[i][k] + G[k][j])

floyd_warshall()
print(G)

