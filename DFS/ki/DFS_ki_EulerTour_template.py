#ABC213D
import sys
sys.setrecursionlimit(300000)

N = int(input())
L = [[] for i in range(N+1)]
for i in range(N-1):
  a, b = (int(i) for i in input().split())
  L[a].append(b)
  L[b].append(a)

for i in range(N+1):
  L[i].sort()

def dfs(crr, pre):
  print(crr)

  for nxt in L[crr]:
    if nxt != pre:
      dfs(nxt, crr)
      print(crr)

dfs(1, 0)

