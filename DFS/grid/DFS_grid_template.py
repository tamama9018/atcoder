H, W = (int(i) for i in input().split())
C = []
for i in range(H):
  C.append(input())
MAP = [[0] * W for _ in range(H)]

def dfs(x, y):

  MAP[x][y] = 1
  for (i, j) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
      nextx = x + i
      nexty = y + j
      if (0 <= nextx) and (nextx <= H-1):
        if (0 <= nexty) and (nexty <= W-1):

          if C[nextx][nexty] == 'g':
            print('Yes')
            exit()
          if C[nextx][nexty] == '.':
            if MAP[nextx][nexty] == 0:
              dfs(nextx, nexty)
              
for i in range(H):
  for j in range(W):
    if C[i][j] == 's':
      startx = i
      starty = j
import sys
sys.setrecursionlimit(200000)
dfs(startx, starty)
print('No')
