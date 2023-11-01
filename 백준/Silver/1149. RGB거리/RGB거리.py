import sys
sys.setrecursionlimit(10**6)

n = int(input())
costs = []
for i in range(n):
    costs.append(list(map(int, input().split())))
    
memos = {}
def cal_min_cost(arr, ban):	
	key = (len(arr), ban)
	if key in memos:
		return memos[key]

	if len(arr) == 1:
		if ban == 0:
			min_cost = min(arr[0][1], arr[0][2])
		elif ban == 1:
			min_cost = min(arr[0][0], arr[0][2])
		elif ban == 2:
			min_cost = min(arr[0][0], arr[0][1])
		memos[key] = min_cost
		return min_cost
	
	if ban == 0:
		min_cost = min(cal_min_cost(arr[1:], 1) + arr[0][1], cal_min_cost(arr[1:], 2) + arr[0][2])
	elif ban == 1:
		min_cost = min(cal_min_cost(arr[1:], 0) + arr[0][0], cal_min_cost(arr[1:], 2) + arr[0][2])
	elif ban == 2:
		min_cost = min(cal_min_cost(arr[1:], 0) + arr[0][0], cal_min_cost(arr[1:], 1) + arr[0][1])
	
	memos[key] = min_cost
	return min_cost

min_cost = min([cal_min_cost(costs, 0), cal_min_cost(costs, 1), cal_min_cost(costs, 2)]) 

print(min_cost)