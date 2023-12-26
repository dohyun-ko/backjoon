def check(n, nums, a, b):
    for i in range(n - 1):
        if nums[i] * a + b != nums[i + 1]:
            return False

    return True


def main():
    n = int(input())

    nums = []
    for i in input().split():
        nums.append(int(i))

    answers = set()

    if n == 1:
        print("A")
        return

    for i in range(-201, 201):
        a = i
        b = nums[1] - nums[0] * a
        if check(n, nums, a, b):
            answers.add(nums[n - 1] * a + b)

    if len(answers) > 1:
        print("A")
        return

    if len(answers) == 0:
        print("B")
        return

    print(answers.pop())


if __name__ == "__main__":
    main()
