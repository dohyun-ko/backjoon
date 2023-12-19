n = int(input())
X = []

def add_decreasing_nums(start_at, length):
  if length == 1:
    return [start_at]

  result = []

  for i in range(0, start_at):
    result = [*result, *list(map(lambda x: start_at * (10 ** (length - 1)) + x, add_decreasing_nums(i, length - 1)))]

  return result
X = [0]

for i in range(1, 11):
  for j in range(1, 10):
    X = [*X, *add_decreasing_nums(j, i)]
try:
  print(X[n])
except:
  print(-1)