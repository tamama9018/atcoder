def ruisekiwa(L):
  ret = [L[0]]
  for l in L[1:]:
    ret.append(ret[-1] + l)
  return ret
