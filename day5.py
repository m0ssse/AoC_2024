def part1(rules, data):
    res = 0
    for line in data:
        nums = [int(x) for x in line.split(",")]
        if validate_line(rules, nums):
            res+=nums[len(nums)//2]
    print(res)

def part2(rules, data):
    res = 0
    for line in data:
        nums = [int(x) for x in line.split(",")]
        if not validate_line(rules, nums):
            fix_nums(rules, nums)
            res+=nums[len(nums)//2]
    print(res)

def fix_nums(rules, nums):
    while not check_and_swap(rules, nums):
        pass

def validate_line(rules, nums):
    for i in range(len(nums)):
        for j in range(i):
            if (nums[i], nums[j]) in rules:
                return False
    return True

def check_and_swap(rules, nums):
    for i in range(len(nums)):
        for j in range(i):
            if (nums[i], nums[j]) in rules:
                nums[i], nums[j] = nums[j], nums[i]
                return False
    return True

fname = "day5_input.txt"
with open(fname) as inputfile:
    rules_str, manuals = inputfile.read().split("\n\n")
rules_set=set()
for line in rules_str.split("\n"):
    y, z = [int(x) for x in line.split("|")]
    rules_set.add((y, z))
manuals = manuals.split("\n")
part1(rules_set, manuals)
part2(rules_set, manuals)