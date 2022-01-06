# ABC029C
n = int(input())

def dfs(s, l):
  if l == n:
    print(s)
    return
  for nxt in [s+'a', s+'b', s+'c']:
    dfs(nxt, l+1)
dfs('a', 1)
dfs('b', 1)
dfs('c', 1)

