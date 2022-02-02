# L[cur] = [nxt, ...]
#     グラフG上で頂点curが隣接する辺集合

from heapq import heappush, heappop, heapify
USED = [0] * (N + 1)
Q = [(dist, nxt) for nxt, dist in L[0]]
USED[0] = 1
heapify(Q)

ans = 0
while Q:
    d, cur = heappop(Q)
    if USED[cur]:
        continue
    USED[cur] = 1
    ans += d
    for nxt, dist in L[cur]:
        if USED[nxt]:
            continue
        heappush(Q, (dist, nxt))

