# AGC033A
H, W = (int(i) for i in input().split())
C = []
for i in range(H):
  C.append(input())
MAP = [[0] * W for _ in range(H)]
TIME = [[0] * W for _ in range(H)]
ans = 0
from collections import deque
def bfs():
  q = deque([])
  for i in range(H):
    for j in range(W):
      if C[i][j] == '#':
        q.append((i, j))
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
bfs()
for i in range(H):
  for j in range(W):
    ans = max(ans, TIME[i][j])
print(ans)
