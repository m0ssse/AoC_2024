def part1(fname):
    res=0
    with open(fname) as inputfile:
        for i, line in enumerate(inputfile):
            nums = [int(x) for x in line.split()]
            safety = is_safe(nums)
#            if safety:
#                print (f"line {i+1} is safe")
            res+=safety
    return res

def part2(fname):
    res = 0
    with open(fname) as inputfile:
        for i, line in enumerate(inputfile):
            nums = [int(x) for x in line.split()]
            line_is_safe = is_safe(nums)
            if line_is_safe:
                res+=1
                #print(f"line {i+1} is safe")
                continue
            for j in range(len(nums)):
                line_without_num = nums[:]
                line_without_num.pop(j)
                helper = is_safe(line_without_num)
                if helper:
                    #print(f"line {i+1} is safe")
                    res+=1
                    break
    return res

def is_safe(nums):
    d = nums[1]-nums[0]
    for i in range(1, len(nums)):
        if d*(nums[i]-nums[i-1])<=0 or abs(nums[i]-nums[i-1])>3:
            return False
    return True
            
fname = "day2_input.txt"
print(part1(fname))
print(part2(fname))