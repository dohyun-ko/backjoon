N, search_range, M= map(int, input().split())
item_nums = [0] + list(map(int, input().split()))
distances = [[] for j in range(N + 1)]
for _ in range(M):
  a, b, c = map(int, input().split())
  distances[a].append((c, b))
  distances[b].append((c, a))
import heapq


def dijkstra(start, distances):
  from_start = [float('inf')] * (N + 1)
  from_start[start] = 0
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
  
  return from_start
max_items = 0

for i in range(1, N + 1):
  item_sum = 0
  i_distances = dijkstra(i, distances)
  for j in range(1, N + 1):
    if i_distances[j] <= search_range:
      item_sum += item_nums[j]

  max_items = max(max_items, item_sum)
print(max_items)