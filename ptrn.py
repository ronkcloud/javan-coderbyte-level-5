def PatternChaser(s):

  # code goes here
  res = []
  for k in range (2,len(s)):
    m = []
    for i in range(len(s)-1):
      m.append(s[i:i+k])

    r = []
    v = []
    for idx_i, i in enumerate(m):
      for idx_j, j in enumerate(m):
        if i == j and idx_i!=idx_j and i not in v:
          r.append(i)
          v.append(i)
          v.append(j)
    for l in r:
      if l not in res:
        res.append(l)

  if len(res) != 0:
    res2 = [i for i in res if len(res[-1]) == len(i)]
    if len(res2) != 0:
      res2 = sorted(res2)
      return 'yes '+''.join(res2[0])
    else:
      return 'yes '+''.join(res[-1])
  else:
    return 'no null'

# keep this function call here 
print(PatternChaser(input()))
"""
1. For input "abcdef12kkk12" the output was incorrect. The correct output is yes 12
"""