from itertools import product
import time

def part1(nums, N):
    res = 0
    for num in nums:
        res+=generate(num, N)[-1]
    print(res)
def generate(x, N):
    res = [x]
    for _ in range(N):
        x=((64*x)^x)%16777216 #2^24
        x=((x//32)^x)%16777216
        x=((2048*x)^x)%16777216
        res.append(x)
    return res

def part2(nums, N):
    totals = {}
    for num in nums:
        seq = generate(num, N)
        change_seq = []
        seen = set()
        for i in range(1, len(seq)):
            change_seq.append(seq[i]%10-seq[i-1]%10)
            if len(change_seq)>=4:
                subseq = tuple(change_seq[-4:])
                if subseq in seen:
                    continue
                seen.add(subseq)
                if subseq not in totals:
                    totals[subseq]=0
                totals[subseq]+=seq[i]%10
    print(max(totals.values()))
        

fname = "day22_input.txt"
with open(fname) as file:
    nums = [int(x) for x in file.read().split()]


part1(nums, 2000)
part2(nums, 2000)