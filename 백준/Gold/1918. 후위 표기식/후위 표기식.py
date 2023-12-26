formula = list(input().strip())
def to_post(formula):
  lf = len(formula)

  i = 0

  while i < lf:
    if formula[i] == "*":
      result = formula[i - 1] + formula[i + 1] + formula[i]
      formula[i - 1] = result
      
      del formula[i]
      del formula[i]
      i -= 1

    elif formula[i] == "/":
      result = formula[i - 1] + formula[i + 1] + formula[i]
      formula[i - 1] = result
    
      del formula[i]
      del formula[i]
      i -= 1

    lf = len(formula)
    i += 1

  i = 0

  while i < lf:
    if formula[i] == "+":
      result = formula[i - 1] + formula[i + 1] + formula[i]
      formula[i - 1] = result
      
      del formula[i]
      del formula[i]
      i -= 1

    elif formula[i] == "-":
      result = formula[i - 1] + formula[i + 1] + formula[i]
      formula[i - 1] = result
    
      del formula[i]
      del formula[i]
      i -= 1

    lf = len(formula)
    i += 1
  
  return formula
right_p = None
left_p = None

lf = len(formula)

i = 0
while i < lf:
  if formula[lf-i-1] == ")":
    right_p = lf-i-1
  if formula[lf-i-1] == "(":
    left_p = lf-i-1
    formula[left_p] = to_post(formula[left_p + 1:right_p])[0]
    formula = formula[:left_p+1] + formula[right_p+1:]
  
    lf = len(formula)
    i = 0
  
  i += 1
print(to_post(formula)[0])