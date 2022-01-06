# ABC126D
import sys
sys.setrecursionlimit(200000)


N = int(input())
L = [[] for i in range(N+1)]
for i in range(N-1):
  u, v, w = (int(i) for i in input().split())
  L[u].append((v, w))
  L[v].append((u, w))
# print(L)
MAP = [-1 for i in range((N+1))]

def dfs(n, weight, prevcolor):
  if weight % 2 == 0 :
    MAP[n] = prevcolor
  else:
    MAP[n] = 1 - prevcolor
    
  for next_node, weight in L[n]:
    if MAP[next_node] < 0:
      dfs(next_node, weight, MAP[n])
  
dfs(1, 0, 0)
# print(MAP)
for i in MAP[1:]:
  print(i)
