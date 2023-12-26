N, M= map(int, input().split())
X = int(input())
distances = [[] for j in range(N + 1)]
for _ in range(M):
  a, b, c = map(int, input().split())
  distances[a].append((c, b))
import heapq

from_start = [float('inf')] * (N + 1)

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
        heapq.heappush(q, (cost, e))
from_start[X] = 0
dijkstra(X, distances)
for i in range(1, N + 1):
  print(from_start[i] if not from_start[i] == float("inf") else "INF")