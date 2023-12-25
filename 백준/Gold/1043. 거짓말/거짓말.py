num_of_people, num_of_party = map(lambda x: int(x), input().split(" "))
line = list(map(lambda x: int(x), input().split(" ")))
know_the_truth = line[1:line[0] + 1]
graph = [[i] for i in range(num_of_people + 1)]
parties = []

for i in range(num_of_party):
  line = list(map(lambda x: int(x), input().split(" ")))
  participants = line[1:line[0] + 1]
  for j in participants:
    for k in participants:
      if not k in graph[j] and k != j:
        graph[j].append(k)
  # print(participants)
  # print(graph)

  parties.append(participants)
def DFS(i, visited):
  friends = []
  for friend in graph[i]:
    if not friend in visited and i != friend:
      visited.append(friend)
      friends = friends + DFS(friend, visited)

  
  return visited
friends_of_friends = [DFS(i, []) for i in range(num_of_people + 1)]
counter = 0

for party in parties:
  someone_know_truth = 0
  for participant in party:
    if participant in know_the_truth:
      someone_know_truth += 1
    for friend in friends_of_friends[participant]:
      if friend in know_the_truth:
        someone_know_truth += 1
  if someone_know_truth < 1:
    counter += 1

print(counter)