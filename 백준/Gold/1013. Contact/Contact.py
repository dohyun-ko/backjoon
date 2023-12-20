n = int(input())

S = []
for i in range(n):
  S.append(input())
def find_pattern(s):
  if len(s) == 0:
    return

  if s[0] == '0' and s[1] == '1':
    find_pattern(s[2:])
  elif s[0] == '1' and s[1] == '0' and s[2] == '0':
    s_index = 3
    while s_index < len(s):
      if s[s_index] == '0':
        s_index += 1
      else:
        break
    
    if s[s_index] == '1':
      succeed = False
      while s[s_index] == '1':
        try:
          find_pattern(s[(s_index + 1):])
          succeed = True
          break
        except:
          s_index += 1
          continue
      if not succeed:
        raise

    else:
      raise
    
  else:
    raise



  
for s in S:
  if len(s) > 0:
    try:
      find_pattern(s)
      print("YES")
    except:
      print("NO")
  else:
    print("NO")