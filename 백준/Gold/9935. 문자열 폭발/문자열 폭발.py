target = list(input())
bomb = input()
len_bomb = len(bomb)
temp = []
done = []

bomb_index = 0

while target:
  popped = target.pop()

  if popped == bomb[len_bomb - bomb_index - 1]:
    bomb_index += 1
    temp.append((popped, bomb_index))

    if bomb_index == len_bomb:
      for i in range(len_bomb):
        temp.pop()
      bomb_index = temp[-1][1] if temp else 0
  else:
    bomb_index = 0
    if popped == bomb[len_bomb - bomb_index - 1]:
      bomb_index += 1
      temp.append((popped, bomb_index))
    else:
      temp = temp[::-1]
      while temp:
        done.append(temp.pop()[0])
      temp = []
      done.append(popped)

temp = temp[::-1]
while temp:
  done.append(temp.pop()[0])
temp = []
print("".join(done[::-1]) if done else "FRULA")