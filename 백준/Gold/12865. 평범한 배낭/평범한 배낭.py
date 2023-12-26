N, K = map(int, input().split())

items = [(0, 0)]
for i in range(N):
  w, v = map(int, input().split())
  items.append((w, v))
items.sort()
table = [[0 for i in range(K+1)] for j in range(N+1)]
for i in range(1, N + 1):
  weight, value = items[i]
  for j in range(1, K + 1):
    if j - weight >= 0:
      table[i][j] = max(table[i-1][j], table[i][j-1], table[i-1][j-weight] + value)
    else:
      table[i][j] = max(table[i-1][j], table[i][j-1])
print(table[N][K])