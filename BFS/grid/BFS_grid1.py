H, W = (int(i) for i in input().split())
C = []
for i in range(H):
  C.append(input())
MAP = [[0] * W for _ in range(H)]
TIME = [[0] * W for _ in range(H)]
from collections import deque
def bfs(x, y):
  q = deque([])
  MAP[x][y] = 1
  q.append((x, y))
  while q:
    cx, cy = q.popleft()
    for (i, j) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
      nextx, nexty = cx+i, cy+j
      if 0 <= nextx <= H-1:
        if 0 <= nexty <= W-1:
          if C[nextx][nexty] == '.':
            if MAP[nextx][nexty] == 0:
              MAP[nextx][nexty] = 1
              TIME[nextx][nexty] = TIME[cx][cy] + 1
              q.append((nextx, nexty))
bfs(0, 0)
print(TIME)
            
  
