def check1(i, curr_result, numbers, target):
    if i==len(numbers):
        return curr_result==target
    num = numbers[i]
    res1 = curr_result*num
    res2 = curr_result+num
    return check1(i+1, res1, numbers, target) or check1(i+1, res2, numbers, target)

def check2(i, curr_result, numbers, target):
    if i==len(numbers):
        return curr_result==target
    num = numbers[i]
    res1 = curr_result*num
    res2 = curr_result+num
    res3 = int(f"{curr_result}{num}")
    return check2(i+1, res1, numbers, target) or check2(i+1, res2, numbers, target) or check2(i+1, res3, numbers, target)

def solve(fname, checkerfun):
    res = 0
    with open(fname) as file:
        for line in file:
            target, nums = line.split(":")
            target = int(target)
            nums = [int(x) for x in nums.split()]
            if checkerfun(1, nums[0], nums, target):
                res+=target
    print(res)

fname = "day7_input.txt"
solve(fname, check1)
solve(fname, check2)