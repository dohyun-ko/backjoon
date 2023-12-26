N = int(input())
sea = []
for i in range(N):
  sea.append(list(map(int, input().split())))
shark = (2, None)
shark_tummy = 0
time = 0
fishes = []
for i in range(N):
  for j in range(N):
    if sea[i][j] == 9:
      shark = (shark[0], (i, j))
      sea[i][j] = 0
    elif sea[i][j] > 0:
      fishes.append((sea[i][j], (i, j)))
from collections import deque

while True:
  q = deque([])
  q.append((shark[1], 0))

  visited = []
  feeds = []

  while q:
    now, time_to_here = q.popleft()

    if now in visited:
      continue

    visited.append(now)

    if sea[now[0]][now[1]] > 0 and sea[now[0]][now[1]] < shark[0]:
      cost = time_to_here
      feeds.append((cost, now))


    adjs = []
    if now[0] > 0:
      adjs.append((now[0] - 1, now[1]))
    if now[1] > 0:
      adjs.append((now[0], now[1] - 1))
    if now[0] < N - 1:
      adjs.append((now[0] + 1, now[1]))
    if now[1] < N - 1:
      adjs.append((now[0], now[1] + 1))

    for adj in adjs:
      if not adj in visited and sea[adj[0]][adj[1]] <= shark[0]:
        q.append((adj, time_to_here + 1))

  if feeds:
    target = min(feeds, key=lambda x: (x[0], x[1][0], x[1][1]))
    shark_tummy += 1
    if shark_tummy >= shark[0]:
      shark_tummy = 0
      shark = (shark[0] + 1, shark[1])
    sea[target[1][0]][target[1][1]] = 0
    shark = (shark[0], target[1])
    time += target[0]
  else:
    break
print(time)