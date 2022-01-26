import bisect
ans = bisect.bisect(L, key)
if ans == n:
  print(-1)
else:
  print(ans)
