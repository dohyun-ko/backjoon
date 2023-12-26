N = int(input())
M = int(input())
distances = [[] for j in range(N + 1)]
for _ in range(M):
  a, b, c = map(int, input().split())
  distances[a].append((c, b))

start, end = map(int, input().split())
import heapq

from_start = [float('inf')] * (N + 1)
paths = [[] for _ in range(N + 1)]


def dijkstra(start, distances):
  q = []
  heapq.heappush(q, (0, start))

  while q:
    dist, now = heapq.heappop(q)

    if from_start[now] < dist:
      continue

    for c, e in distances[now]:
      cost = dist + c

      if cost < from_start[e]:
        from_start[e] = cost
        paths[e] = paths[now][:] + [e]
        heapq.heappush(q, (cost, e))
from_start[start] = (0)
paths[start] = [start]
dijkstra(start, distances)
print(from_start[end])
print(len(paths[end]))
for city in paths[end]:
  print(city, end=" ")