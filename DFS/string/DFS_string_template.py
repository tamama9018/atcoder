#ABC161D
import sys
sys.setrecursionlimit(300000)

k = int(input())
l = []
def dfs(n, keta):
  l.append(n)
  if keta == 10:
    return
  lastn = n%10
  if lastn == 9:
    next_list = [n*10+lastn-1, n*10+lastn]
  elif lastn == 0:
    next_list = [n*10+lastn, n*10+lastn+1]
  else:
    next_list = [n*10+lastn-1, n*10+lastn, n*10+lastn+1]
  for nxt in next_list:
    dfs(nxt, keta+1)


for i in range(1,10):
  dfs(i, 1)
l.sort()
print(l[k-1])
