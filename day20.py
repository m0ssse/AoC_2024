def part1(grid, thresh):
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char=="S":
                starti, startj = i, j
            if char=="E":
                targeti, targetj = i, j
    dist = bfs(grid, starti, startj)
    T = dist[(targeti, targetj)]
    res = 0
    for i, j in dist:
        for ii, jj in [(i-2, j), (i+2, j), (i, j-2), (i, j+2), (i+1, j+1), (i+1, j-1), (i-1, j+1), (i-1, j-1)]:
            if (ii, jj) not in dist:
                continue
            #total_time = dist[(i, j)]+T-dist[(ii, jj)]+2
            time_save = dist[(ii, jj)]-dist[(i, j)]-2
            if time_save>=thresh:
                res+=1
    print(res)

def part2_dumb(grid, thresh, maxd):
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char=="S":
                starti, startj = i, j
            if char=="E":
                targeti, targetj = i, j
    dist = bfs(grid, starti, startj)
    res = 0
    for i, j in dist:
        for i2, j2 in dist:
            d = abs(i-i2)+abs(j-j2)
            if d>maxd:
                continue
            time_save = dist[(i2, j2)]-dist[(i, j)]-d
            if time_save>=thresh:
                res+=1
    print(res)

def bfs(grid, starti, startj):
    n, m = len(grid), len(grid[0])
    dist = [[0]*m for _ in range(n)]
    queue = [(starti, startj)]
    dist = {(starti, startj): 0}
    k = 0
    while k<len(queue):
        i, j = queue[k]
        k+=1
        for ii, jj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if grid[ii][jj]=="#" or (ii, jj) in dist:
                continue
            dist[(ii, jj)] = dist[(i, j)]+1
            queue.append((ii, jj))
    return dist

#fname, thresh = "day20_test.txt", 50
fname, thresh = "day20_input.txt", 100
with open(fname) as file:
    grid = file.read().split()
part1(grid, thresh)
part2_dumb(grid, thresh, 20)