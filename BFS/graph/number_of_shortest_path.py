# ABC211D 
n,m = (int(i) for i in input().split())
L = [[] for i in range(n+1)]
for i in range(m):
  a,b = (int(i) for i in input().split())
  L[a].append(b)
  L[b].append(a)
MAP = [0] * (n+1)
TIME = [0] * (n+1)
PATH = [0] * (n+1)
from collections import deque
def bfs(first):
  q = deque([])
  MAP[first] = 1
  PATH[first] = 1
  q.append(first)
  while q:
    cn = q.popleft()
    for nextn in L[cn]:
      if MAP[nextn] == 0:
        MAP[nextn] = 1
        TIME[nextn] = TIME[cn] + 1
        PATH[nextn] = PATH[cn]
        q.append(nextn)
      elif TIME[nextn] == TIME[cn] + 1:
        PATH[nextn] += PATH[cn]
        PATH[nextn] %= 10**9+7
bfs(1)
print(PATH[n])
            
  


