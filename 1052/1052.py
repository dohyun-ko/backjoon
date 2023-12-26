n, k = list(map((lambda x: int(x)), input().split(" ")))
bottles = [n]

bought = 0


for i in range(len(bottles) - 1):
    bottles[i + 1] += bottles[i] // 2
    bottles[i] = bottles[i] % 2

if bottles[-1] // 2:
    bottles.append(bottles[-1] // 2)
    bottles[-2] %= 2

while sum(bottles) > k:
    bought += 1
    bottles[0] += 1

    for i in range(len(bottles) - 1):
        bottles[i + 1] += bottles[i] // 2
        bottles[i] = bottles[i] % 2

    if bottles[-1] // 2:
        bottles.append(bottles[-1] // 2)
        bottles[-2] %= 2

print(bought)
