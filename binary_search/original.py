n,k = (int(i) for i in input().split())
A = [int(i) for i in input().split()]
def is_ok(mid):
  """ 返り値を変える """
  return A[mid] >= k

def bin_search(ok, ng):
  while abs(ng-ok) > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
      ok = mid
    else:
      ng = mid
  return ok

print(bin_search(n-1, 0))
