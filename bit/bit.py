s = input()
N = 3
ans = 0
for i in range(2**N): 
  L = []
  for j in range(N):
    L.append(i//2**j % 2)
  siki = s[0]
  for l, s_ in zip(L, s[1:]):
    if l:
      siki += '+'
    else:
      siki += '-'
    siki += s_
  if eval(siki) == 7:
    print(siki + '=7')
    exit()
    