def hanoi_print(fr, to, empty, num):
    if num <= 0:
        return;
    hanoi_print(fr, empty, to, num - 1)
    
    print(str(fr) + " " + str(to))
    
    hanoi_print(empty, to, fr, num - 1)
    
def hanoi(n):
    if n <= 0:
        return 0
    return hanoi(n - 1) * 2 + 1


n = int(input())

print(hanoi(n))

if n <= 20:
    hanoi_print(1, 3, 2, n)
