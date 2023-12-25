N, M, X = map(int, input().split())
distances = [[(float("inf"), i) for i in range(N + 1)] for j in range(N + 1)]
distances_reversed = [[(float("inf"), i) for i in range(N + 1)] for j in range(N + 1)]
for _ in range(M):
  a, b, c = map(int, input().split())
  distances[a][b] = (c, b)
  distances_reversed[b][a] = (c, a)
import heapq

def dijkstra(start, distances):
  q = distances[start].copy()

  heapq.heapify(q)

  while q:
    dist, now = heapq.heappop(q)

    if distances[start][now][0] < dist:
      continue

    for c, e in distances[now]:
      cost = dist + c

      if cost < distances[start][e][0]:
        distances[start][e] = (cost, e)
        heapq.heappush(q, (cost, e))
for i in range(N + 1):
  distances[i][i] = (0, i)
  distances_reversed[i][i] = (0, i)
dijkstra(X, distances)
dijkstra(X, distances_reversed)
max_dist = 0
for i in range(1, N + 1):
  max_dist = max(distances[X][i][0] + distances_reversed[X][i][0], max_dist)
print(max_dist)