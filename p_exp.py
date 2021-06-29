def PolynomialExpansion(s):

  # code goes here
  def group (init, c=[]):
    p1 = init.find("(")
    p2 = init.find(")")
    if p1 == -1 or p2 == -1:
      return c

    s = init[p1+1:p2]
    op = []
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
    if len(op) != 0:
      val = ['' for _ in range(len(op)*2)]
      val[0] = s[:op[0]]
      val[1] = s[op[0]:]
      c.append(val)
    else:
      c.append([s])

    return group (init[len(s)+2:], c)
    
  ltr = ""
  for i in s:
    if i.isalpha():
      ltr = i
      break

  c = group (s)
  z = [(i,j) for i in c[0] for j in c[1]]
  print (z)
  r = []
  for i in z:
    k = []
    p = []
    c = []
    for j in i:
      if ltr in j:
        k.append(j[:j.find(ltr)])
      if ltr not in j:
        # for a in i:
        #   if ltr in a:
        #     break
        # else:
        k.append(j)
      if ltr in j and '^' not in j:
        j += '^1'
      if '^' in j:
        p.append(j[j.find('^')+1:])
    if len(k) != 0:
      k = eval("*".join(k))
      if k == 1:
        k = 'x'
      else:
        k = str(k)+'x'
    if len(p) != 0:
      p = eval("+".join(p))
      if p == 1:
        p = ''
      else:
        p = '^'+str(p)
    if len(p) !=0 and len(k)!=0:
      r.append(k+p)
    elif len(p) !=0:
      r.append(p)
    elif len(k) !=0:
      r.append(k)

  print (r)

  # lar = 0
  # for i in r:
  #   if '^' in i:
  #     p = i[i.find('^'):]


  # return 

print(PolynomialExpansion("(2x^2+4)(6x^3+3)"))

"""
Input: "(1x)(2x^-2+1)"
Output: x+2x^-1
Input: "(-1x^3)(3x^3+2)"
Output: -3x^6-2x^3
(2x^2+4)(6x^3+3)", then the output should be "12x^5+24x^3+6x^2+12"
"""
  # if "^" in s:
  #   pvl = [idx for idx,i in enumerate(s) if i == "^"]
    
  #   for idx, i in enumerate(pvl):
  #     if not s[i+1].isdigit():
  #       pv = s[i+1:i+3]
  #     else:
  #       pv = s[i+1]
  #     pvl[idx] = pv
    
  #   print (pvl)