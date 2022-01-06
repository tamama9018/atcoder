# ABC209D

import sys
sys.setrecursionlimit(200000)

N, Q = (int(i) for i in input().split())
L = [[] for i in range(N+1)]
for i in range(N-1):
  a, b = (int(i) for i in input().split())
  L[a].append(b)
  L[b].append(a)
# print(L)
MAP = [-1 for i in range((N+1))]

def dfs(n, prevcolor):
  MAP[n] = 1 - prevcolor
    
  for next_node in L[n]:
    if MAP[next_node] < 0:
      dfs(next_node, MAP[n])
  
dfs(1, 1)
# print(MAP)
for j in range(Q):
  c, d = (int(i) for i in input().split())
  if MAP[c] == MAP[d]:
    print('Town')
  else:
    print('Road')
