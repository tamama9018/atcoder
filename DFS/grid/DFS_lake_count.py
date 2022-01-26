# Lake Counting
# 蟻本p35

h,w = (int(i) for i in input().split())
C = [list(input()) for i in range(h)]
MAP = [[0]*w for i in range(h)]

def dfs(x, y):
  MAP[x][y] = 1
  C[x][y] = '.'
  for (i,j) in [(1,0), (1,1), (1,-1), (0,1), (0,-1), (-1,1), (-1,0), (-1,-1)]:
    nextx = x + i
    nexty = y + j
    if 0 <= nextx <= h-1:
      if 0 <= nexty <= w-1:
        if C[nextx][nexty] == 'W':
          if MAP[nextx][nexty] == 0:
            dfs(nextx, nexty)
ans = 0            
for i in range(h):
  for j in range(w):
    if C[i][j] == 'W':
      dfs(i,j)
      ans += 1
      
print(ans)      
  
