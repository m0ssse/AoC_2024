def blink(n):
    if n==0:
        return [1]
    elif len(str(n))%2==0:
        n = str(n)
        l = len(n)//2
        return [int(n[:l]), int(n[l:])]
    return [2024*n]

def solve(stones, blinks):
    stone_counts = {}
    for stone in stones:
        if stone not in stone_counts:
            stone_counts[stone]=0
        stone_counts[stone]+=1
    for _ in range(blinks):
        new_counts = {}
        for stone, n in stone_counts.items():
            for new_stone in blink(stone):
                if new_stone not in new_counts:
                    new_counts[new_stone]=0
                new_counts[new_stone]+=n
        stone_counts = new_counts
    print(sum(stone_counts.values()))

fname = "day11_input.txt"
with open(fname) as file:
    stones = [int(x) for x in file.read().split()]
solve(stones, 75)