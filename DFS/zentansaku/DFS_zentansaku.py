# 部分和問題
# 蟻本p34 
n, k = (int(i) for i in input().split())
A = [int(i) for i in input().split()]
L = [0] * n
def dfs(sum, i):
  if i == n:
    if sum == k:
      print('Yes')
      exit()
    else:
      return 0
  dfs(sum + A[i], i+1)
  dfs(sum, i+1)
  
dfs(0, 0)
print('No')
