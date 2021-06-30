def PolynomialExpansion(s):

  # code goes here
  def zero_p_check (r):
    for idx, i in enumerate(r):
      if 'x^0' in i:
        r[idx] = i[:i.find(ltr)]
        break
      else:
        return r
    add = []
    for idx, i in enumerate(r):
      if '^' not in i and ltr not in i:
        add.append(i)
        del r[idx]
    r.append(str(eval('+'.join(add))))
    return r 

  def group (init, c=[]):
    p1 = init.find("(")
    p2 = init.find(")")
    if p1 == -1 or p2 == -1:
      return c

    s = init[p1+1:p2]
    op = [0]
    s += ' '
    for idx, i in enumerate(s):
      if i.isdigit():
        d = s[idx+1]
        if d == '+' or d == '-':
          op.append(idx+1)
      elif i.isalpha():
        d = s[idx+1]
        if d == '+' or d == '-':
          op.append(idx+1)
    s = s.replace(' ', '')
    op.append(len(s))
    c.append([s[op[i-1]:op[i]] for i in range(1,len(op))])
    return group (init[len(s)+2:], c)
    
  ltr = ""
  for i in s:
    if i.isalpha():
      ltr = i
      break

  c = group (s)
  z = [(i,j) for i in c[0] for j in c[1]]

  r = []
  for i in z:
    k = []
    p = []
    c = []
    for j in i:
      if ltr in j:
        k.append(j[:j.find(ltr)])
      if ltr not in j:
        status = False
        for a in i:
          if ltr in a:
            status = True
        if status == True:
          k.append(j)
        else:
          c.append(j)
      if ltr in j and '^' not in j:
        j += '^1'
      if '^' in j:
        p.append(j[j.find('^')+1:])
    if len(k) != 0:
      k = eval("*".join(k))
      if k == 1:
        k = ltr
      else:
        k = str(k)+ltr
    if len(p) != 0:
      p = eval("+".join(p))
      if p == 1:
        p = ''
      else:
        p = '^'+str(p)
    if len(c) !=0:
      c = str(eval("*".join(c)))
    if len(p) !=0 and len(k)!=0:
      r.append(k+p)
    elif len(p) !=0:
      r.append(p)
    elif len(k) !=0:
      r.append(k)
    elif len(c) !=0:
      r.append(c)

  zero_p_check (r)
  for idx_i, i in enumerate(r):
    if '^' in i:
      p = i[i.find('^')+1:]
      for idx_j, j in enumerate(r):
        if '^' in j:
          p2 = j[j.find('^')+1:]
          if p == p2 and idx_i!=idx_j:
            b = i[:i.find(ltr)]+'+'+j[:j.find(ltr)]
            if len(b) == 1:
              b = '2'
            r[idx_i] = str(eval(b))+ltr+'^'+p
            del r[idx_j]

  for i in range(1,len(r)):
    res = r[i][:]
    if '^' in r[i]:
      key = r[i][r[i].find('^')+1:]
    elif '^' not in r[i] and ltr in r[i]:
      key = 1
    else:
      key = 0
    
    j = i-1
    if '^' in r[j]:
      d = r[j][r[j].find('^')+1:]
    elif '^' not in r[j] and ltr in r[j]:
      d = 1
    else:
      d = 0
    while j >= 0 and int(key)>int(d):
      r[j+1] = r[j]
      j-=1
      if '^' in r[j]:
        d = r[j][r[j].find('^')+1:]
      elif '^' not in r[j] and ltr in r[j]:
        d = 1
      else:
        d = 0
      r[j+1] = res
  
  for i in range(1, len(r)):
    if r[i][0].isdigit() or r[i][0].isalpha() :
      r[i] = '+'+r[i]

  return ''.join(r)

print(PolynomialExpansion("(-1p^1+3)(-1p^2-1p^2)"))

"""
Input: "(1x)(2x^-2+1)" Output: x+2x^-1
Input: "(-1x^3)(3x^3+2)" Output: -3x^6-2x^3
(2x^2+4)(6x^3+3)" = "12x^5+24x^3+6x^2+12"
1. For input "(1x^5-4x^2+3)(2x^2+3)" = 2x^7+3x^5-8x^4-6x^2+9
2. For input "(1x^2-4)(2x^-2+1)" = x^2-2-8x^-2
3. For input "(1x^3-3)(2x^2+1)" = 2x^5+x^3-6x^2-3
4. For input "(2x^0)(1)" = 2
5. For input "(-1y^10)(-1y^12)" = y^22
6. For input "(-1p^1+3)(-1p^2-1p^2)" = 2p^3-6p^2
"""


