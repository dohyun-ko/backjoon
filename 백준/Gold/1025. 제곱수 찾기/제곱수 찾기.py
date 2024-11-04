N, M = list(map(int, input().split()))

grid = [input() for x in range(N)]
nums = set()

for i in range(N):
  for j in range(M):

    for gap_n in range(-8, 9):
      for gap_m in range(-8, 9):
        num_str = ''

        if gap_n == 0 and gap_m == 0:
          num_str += grid[i][j]
          continue

        new_n = i
        new_m = j

        while 0 <= new_n < N and 0 <= new_m < M:
          num_str += grid[new_n][new_m]

          new_n += gap_n
          new_m += gap_m
          nums.add(int(num_str))
        

nums = sorted(list(nums), reverse=True)
answer = -1

for num in nums:
  if num ** 0.5 % 1 == 0:
    answer = num
    break

print(answer)
