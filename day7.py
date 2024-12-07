def check(i, curr_result, numbers, target, N):
    if i==len(numbers):
        return curr_result==target
    if curr_result>target:
        return False
    num = numbers[i]
    res1 = curr_result*num
    res2 = curr_result+num
    res3 = int(f"{curr_result}{num}")
    return any([check(i+1, res, numbers, target, N) for res in [res1, res2, res3][:N]])

def solve(fname, N):
    res = 0
    with open(fname) as file:
        for line in file:
            target, nums = line.split(":")
            target = int(target)
            nums = [int(x) for x in nums.split()]
            if check(1, nums[0], nums, target, N):
                res+=target
    print(res)

fname = "day7_input.txt"
solve(fname, 2)
solve(fname, 3)
