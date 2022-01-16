# ABC235D
a, N = (int(i) for i in input().split())
MAX = 10**7 + 1
MAP = [0] * MAX
TIME = [0] * MAX
Nlen = len(str(N))
from collections import deque
def rotate(n):
  s = str(n)
  return int(s[-1] + s[:-1])
def bfs(n):
  q = deque([])
  MAP[n] = 1
  q.append(n)
  while q:
    cn = q.popleft()
    if cn >= 10 and cn%10 != 0:
      nextlist = [cn*a, rotate(cn)]
    else:
      nextlist = [cn*a]
                
    for nextn in nextlist:
      if len(str(nextn)) <= Nlen:
        if MAP[nextn] == 0:
          MAP[nextn] = 1
          TIME[nextn] = TIME[cn] + 1
          q.append(nextn)
bfs(1)
dist = TIME[N]
if dist:
  print(dist)
else:
  print(-1)
