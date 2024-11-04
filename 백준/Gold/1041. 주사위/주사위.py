N = int(input())
A, B, C, D, E, F = list(map(int, input().split()))
one_faces = [A, B, C, D, E, F]
two_faces = [A+B, A+D, A+E, A+C,  D+B, B+C, C+E, E+D,  D+F, B+F, C+F, E+F]
three_faces = [A+B+C, A+C+E, A+E+D, A+D+B,  F+B+C, F+C+E, F+E+D, F+D+B]
one = min(one_faces)
two = min(two_faces)
three = min(three_faces)
five = A + B + C + D + E + F - max(one_faces)
sum_of_faces = 0

if N == 1:
  sum_of_faces += five
else:
  sum_of_faces += three * 4
  sum_of_faces += two * ((N-2) * 4 + (N-1) * 4)
  sum_of_faces += one * (N-2) * (N-1) * 4
  sum_of_faces += one * ((N-2) ** 2)

print(sum_of_faces)