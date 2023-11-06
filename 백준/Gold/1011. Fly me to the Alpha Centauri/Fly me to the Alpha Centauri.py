n = int(input())

paths = []

for i in range(n):
	x, y = input().split()
	paths.append((int(x), int(y)))
def decideK(gap):
	k = 1
	while True:
		k_to_1 = (k * (1 + k) / 2) * 2 - k
		if k_to_1 > gap:
			return k - 1
		else:
			k = k + 1
def calculateSteps(x, y):
	gap = y - x
	k = decideK(gap)
	additional = 0
	rest = gap - ((k * (1 + k) / 2) * 2 - k)
	j = k
	while rest > 0:
		if rest >= j:
			rest = rest - j
			additional = additional + 1
		else:
			j = j - 1

	return 2 * k - 1 + additional
for x, y in paths:
	print(calculateSteps(x, y))