def test(funcs, nums):
    is_reversed = False
    try:
        for f in funcs:
            if f == "R":
                is_reversed = not is_reversed
            else:
                if is_reversed:
                    nums.pop()
                else:
                    nums.pop(0)

        if is_reversed:
            nums.reverse()

        print("[", end="")

        for i in range(len(nums)):
            print(nums[i], end="")
            if i != len(nums) - 1:
                print(",", end="")

        print("]")

    except Exception:
        print("error")


def main():
    n = int(input())

    inputs = []

    for _ in range(n):
        funcs = input()
        length = int(input())
        nums = input()
        nums = nums[1 : (len(nums) - 1)]
        nums = nums.split(",")
        nums = [num for num in nums if num != ""]
        inputs.append((funcs, nums))

    for i in inputs:
        funcs, nums = i
        test(funcs, nums)


if __name__ == "__main__":
    main()
