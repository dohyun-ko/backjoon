N = int(input())
blueprint = [[" " for i in range(N*2 - 1)] for j in range(N)]
def triange(height, start_at):
  m, n = start_at
  if height == 3:
    blueprint[m][n] = "*"
    
    blueprint[m + 1][n - 1] = "*"
    blueprint[m + 1][n + 1] = "*"
    
    blueprint[m + 2][n - 2] = "*"
    blueprint[m + 2][n - 1] = "*"
    blueprint[m + 2][n] = "*"
    blueprint[m + 2][n + 1] = "*"
    blueprint[m + 2][n + 2] = "*"
    

    return

  triange(height/2, start_at)
  triange(height/2, (int(m + height/2), int(n - height/2)))
  triange(height/2, (int(m + height/2), int(n + height/2)))
  
triange(N, (0, N - 1))
for line in blueprint:
  for char in line:
    print(char, end="")
  print("")