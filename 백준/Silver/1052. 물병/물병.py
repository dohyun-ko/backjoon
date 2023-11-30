n, k = list(map((lambda x: int(x)), input().split(" ")))
bottles = [n]

bottles[0] = n

bought = 0

i = 0
while i < (l := len(bottles)):
  if  (val := bottles[i] // 2) > 0 and i == l - 1:
    bottles.append(0)
  if val > 0:
    bottles[i + 1] += val
    bottles[i] = bottles[i] % 2
  i += 1


while sum(bottles) > k:
  bought += 1
  bottles[0] += 1

  i = 0
  while i < (l := len(bottles)):
    if (val := bottles[i] // 2) > 0 and i == l - 1:
      bottles.append(0)
    if val > 0:
      bottles[i + 1] += val
      bottles[i] = bottles[i] % 2
    i += 1

print(bought)