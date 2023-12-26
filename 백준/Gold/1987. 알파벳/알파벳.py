R, C = list(map(int, input().split()))
board = []
for i in range(R):
  board.append(input())
stack = [((0, 0), [])]
max_depth = 0
counter = 0

memos = {}

while stack and len(stack) < 100:
  counter += 1
  now, visited = stack.pop()
  # print(now, visited)

  visited.append(board[now[0]][now[1]])

  key = (now, str(visited))

  if key in memos:
    continue

  max_depth = max(max_depth, len(visited))
  memos[key] = max_depth

  m, n = now

  adjs = []

  if m > 0:
    adjs.append((m-1, n))
  if n > 0:
    adjs.append((m, n-1))
  if m < R-1:
    adjs.append((m+1, n))
  if n < C-1:
    adjs.append((m, n+1))

  for adj in adjs:
    if not board[adj[0]][adj[1]] in visited:
      stack.append((adj, visited[:]))
  
print(max_depth)