def Calculator(strParam):

  def clean (x):
    if not x[0].isdigit():
        x = x[1:]
    if not x[len(x)-1].isdigit():
        x = x[:len(x)-1]
    return x
  
  def par (s):
    
    p1 = s.find("(")
    p2 = s.find(")")
    if p1 == -1 or p2 == -1:
        return s

    z = s[p1+1:p2]
    z = ['*',str(eval(z))]
    s = list(s)
    s[p1:p2+1] = z
    s = "".join(s)
    return par (s)
  
  s = strParam
  if "(" in s and ")" in s:
    x = par(s)
    x = clean(x)   
    res = eval(x)
  else:
    res = eval(s)
        
    
  return int(res)

print (Calculator("7-4-1+8(3)/2" ))

"""
1. For input "(4/2)(3-1)" the output was incorrect. The correct output is 4

2. For input "7-4-1+8(3)/2" the output was incorrect. The correct output is 14
"""