def proper_insert(li, a):
    for i in range(len(li)):
        if li[i] < a:
            continue
        else:
            li.insert(i, a)
            return

    li.insert(len(li), a)
    return


li = []

n = int(input())

for i in range(n):
    proper_insert(li, int(input()))
    print(li[(len(li) - 1) // 2])
