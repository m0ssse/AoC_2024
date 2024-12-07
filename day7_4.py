import time

def check(nums, target, to_concatenate):
    n_forwards = len(nums)//2
    n_backwards = len(nums)-n_forwards
    target_as_str = str(target)
    previous_results_forward = {nums[0]}
    previous_results_backwards = {target}
    for i in range(1, n_forwards):
        results_new_forwards = set()
        for n in previous_results_forward:
            if n>target:
                continue
            results_new_forwards.add(n+nums[i])
            results_new_forwards.add(n*nums[i])
            if to_concatenate:
                results_new_forwards.add(int(f"{n}{nums[i]}"))
            previous_results_forward = results_new_forwards
    
    for i in range(n_backwards):
        results_new_backwards = set()
        for n in previous_results_backwards:
            if n<nums[~i]:
                continue
            results_new_backwards.add(n-nums[~i])
            if n%nums[~i]==0:
                results_new_backwards.add(n//nums[~i])
            if to_concatenate and str(n).endswith(str(nums[~i])):
                x, y = len(str(n)), len(str(nums[~i]))
                results_new_backwards.add(int(str(n)[:x-y]))
        previous_results_backwards = results_new_backwards

    for n in previous_results_backwards:
        if n in previous_results_forward:
            return True
    return False    
    

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