# 最長共通部分列(LCS)
s, t = input(), input()
slen, tlen = len(s), len(t)
dp = [[0]*(tlen+1) for i in range(slen+1)]
for i in range(1, slen+1):
  for j in range(1, tlen+1):
    if s[i-1] == t[j-1]:
      dp[i][j] = dp[i-1][j-1] + 1
    else:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#print(dp)
length = dp[slen][tlen]
#print(length)
i, j = slen, tlen
ans = ""
while length > 0:
#  print(s[i-1], t[j-1])
  if s[i-1] == t[j-1]:
    ans += s[i-1]
    i -= 1
    j -= 1
    length -= 1
  elif dp[i][j] == dp[i-1][j]:
    i -= 1
  else:
    j -= 1
    
print(ans[::-1])
