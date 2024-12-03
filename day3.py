import re

def part1(contents):
    pattern = r"mul\(\d+,\d+\)"
    res = 0
    for match in re.findall(pattern, contents):
        x, y = match[4:-1].split(",")
        res+=int(x)*int(y)
    return res

def part2(contents):
    dont_pattern = r"don't\(\)"
    dont_matches = [m.span() for m in re.finditer(dont_pattern, contents)]

    do_pattern = r"do\(\)"
    do_matches = [m.span() for m in re.finditer(do_pattern, contents)]

    triggers = []
    for i, _ in do_matches:
        triggers.append((i, 0))
    for j, _ in dont_matches:
        triggers.append((j, 1))
    triggers.sort()
    triggers_red=[]
    curr_start = 0
    curr_type = 0
    for ind, type in triggers:
        if type!=curr_type:
            triggers_red.append((curr_start, ind, curr_type))
            curr_start = ind
            curr_type=type
    if curr_type == 0:
        triggers_red.append((curr_start, len(contents), curr_type))
    active_ranges = [(i, j) for i, j, k in triggers_red if not k]
    strings_to_consider = [contents[i:j+1] for i, j in active_ranges]
    res=0
    for s in strings_to_consider:
        res+=part1(s)
    return res

with open("day3_input.txt") as inputfile:
    contents = inputfile.read()
print(part1(contents))
print(part2(contents))
