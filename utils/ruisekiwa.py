def ruisekiwa(L):
  ret = [0]
    for l in L:
        ret.append(ret[-1] + l)
          return ret
