N,M,T = (int(i) for i in input().split())
A = [int(i) for i in input().split()]
L = [[] for i in range(N+1)]

for i in range(M):
  a,b,c = (int(i) for i in input().split())
  L[a].append([b, c])
  L[b].append([a, c])

# ダイクストラ法(O(N)=NlogN+M)
import heapq
MAP = [float('inf')] * (N+1)
PREV = [-1] * (N+1)

def djikstra(first):
  Q = [[0, first]]
  MAP[first] = 0
  heapq.heapify(Q)

  while Q:
    d, cur = heapq.heappop(Q)
    for nxt, dist in L[cur]:
      alt = MAP[cur] + dist
      if MAP[nxt] > alt:
        MAP[nxt] = alt
        PREV[nxt] = cur
        heapq.heappush(Q, [alt, nxt])
djikstra(1)
print(MAP)
