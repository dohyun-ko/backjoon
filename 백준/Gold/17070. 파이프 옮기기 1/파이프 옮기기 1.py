N = int(input())
house = []
for i in range(N):
  house.append(list(map(int, input().split())))

stack = [((0, 1), 0)]
num_of_way = 0

# state: horizontal = 0, vertial = 1, diagonal = 2
while stack:
  now, state = stack.pop()
  m, n = now

  if m == N - 1 and n == N - 1:
    num_of_way += 1
    continue


  if state == 0:
    if n == N - 1:
      continue
    if house[m][n + 1] != 1:
      stack.append(((m, n+1), 0))
    if m != N - 1 and house[m][n + 1] != 1 and house[m + 1][n] != 1 and house[m + 1][n + 1] != 1:
      stack.append(((m+1, n+1), 2))
  if state == 1:
    if m == N - 1:
      continue
    if house[m+1][n] != 1:
      stack.append(((m+1, n), 1))
    if n != N - 1 and house[m][n + 1] != 1 and house[m + 1][n] != 1 and house[m + 1][n + 1] != 1:
      stack.append(((m+1, n+1), 2))
  if state == 2:
    if n != N - 1 and house[m][n + 1] != 1:
      stack.append(((m, n+1), 0))
    if m != N - 1 and house[m+1][n] != 1:
      stack.append(((m+1, n), 1))
    if m != N - 1 and n != N - 1 and house[m][n + 1] != 1 and house[m + 1][n] != 1 and house[m + 1][n + 1] != 1:
      stack.append(((m+1, n+1), 2))
  
print(num_of_way)