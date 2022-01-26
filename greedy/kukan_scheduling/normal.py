n = int(input())
task = []
for i in range(n):
  l, r = (int(i) for i in input().split())
  task.append([l, r])

task = sorted(task, key=lambda x:x[1])
cur, nxt = 0, 1
ans = n
while nxt < n and cur < n:
  # 次のと重なってたら次のを消す
  if task[cur][1] > task[nxt][0]:
    ans -= 1
  else:
    cur = nxt
  nxt += 1
print(ans)


