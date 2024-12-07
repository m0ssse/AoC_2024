import time

def check(nums, target, to_concatenate):
    previous_results = {nums[0]}
    for i in range(1, len(nums)):
        results_new = set()
        for n in previous_results:
            if n>target:
                continue
            results_new.add(n+nums[i])
            results_new.add(n*nums[i])
            if to_concatenate:
                results_new.add(int(f"{n}{nums[i]}"))
            previous_results = results_new
    return target in previous_results
def solve(fname):
    res1 = 0
    res2 = 0
    with open(fname) as file:
        for line in file:
            target, nums = line.split(":")
            target = int(target)
            nums = [int(x) for x in nums.split()]
            if check(nums, target, False):
                res1+=target
                res2+=target
            elif check(nums, target, True):
                res2+=target
    print(res1)
    print(res2)
fname = "day7_input.txt"
t = time.time()
solve(fname)
t2 = time.time()
print(t2-t)