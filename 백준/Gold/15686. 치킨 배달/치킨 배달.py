N, M = map(int, input().split())
houses = []
chickens = []

for i in range(N):
  buildings = list(map(int, input().split()))
  for j in range(len(buildings)):
    if buildings[j] == 1:
      houses.append((i, j))
    elif buildings[j] == 2:
      chickens.append((i, j))
def cal_city_cost(chickens):
  city_cost = 0
  for h in houses:
    min_cost = abs(h[0] - chickens[0][0]) + abs(h[1] - chickens[0][1])
    for c in chickens:
      min_cost = min(min_cost, abs(h[0] - c[0]) + abs(h[1] - c[1]))
    city_cost += min_cost
  
  return city_cost
from itertools import combinations

combi = list(combinations(chickens, M))

min_city_cost = float("inf")

for c in combi:
  min_city_cost = min(min_city_cost, cal_city_cost(list(c)))

print(min_city_cost)