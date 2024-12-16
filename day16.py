from heapq import heappush, heappop

def part1(grid):
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char=="S":
                starti, startj = i, j
            if char=="E":
                targeti, targetj = i, j
    visited = set()
    heap = [(0, starti, startj, 0, 1)]

    while heap:
        cost, i, j, di, dj = heappop(heap)
        if (i, j, di, dj) in visited:
            continue
        visited.add((i, j, di, dj))
        if i==targeti and j==targetj:
            return cost
        neighbs = [(1, i+di, j+dj, di, dj), (1000, i, j, -dj, di), (1000, i, j, dj, -di)]
        for neighb_cost, ii, jj, dii, djj in neighbs:
            if grid[ii][jj]=="#" or (ii, jj, dii, djj) in visited:
                continue
            heappush(heap, (cost+neighb_cost, ii, jj, dii, djj))

def part2(grid):
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char=="S":
                starti, startj = i, j
            if char=="E":
                targeti, targetj = i, j
    mincost = part1(grid)
    allpaths = []
    currpath = [(starti, startj, 0, 1)]
    dead_ends = get_dead_ends(grid)
    dfs(starti, startj, 0, 1, targeti, targetj, 0, mincost, currpath, allpaths, dead_ends)
    visited = set()
    for path in allpaths:
        for i, j, _, _ in path:
            visited.add((i, j))
    print(len(visited))

def get_dead_ends(grid):
    dead_ends = set()
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char==".":
                neighb_walls = 0
                for ii, jj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if grid[ii][jj]=="#":
                        neighb_walls+=1
                if neighb_walls==3:
                    dead_ends.add((i, j))
                    dfs_dead_end(grid, i, j, dead_ends)
    return dead_ends

def dfs_dead_end(grid, i, j, dead_ends):
    if grid[i][j] in "SE":
        return
    neighb_walls = 0
    for ii, jj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if grid[ii][jj]=="#":
            neighb_walls+=1
    if neighb_walls<2:
        return
    dead_ends.add((i, j))
    for ii, jj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if grid[ii][jj]!="#" and (ii, jj) not in dead_ends:
            dfs_dead_end(grid, ii, jj, dead_ends)

def dfs(i, j, di, dj, targeti, targetj, currcost, maxcost, currpath, allpaths, dead_ends):
    if currcost>maxcost:
        return
    if i==targeti and j==targetj and currcost==maxcost:
        allpaths.append(currpath[:])
        return
    neighbs = [(1, i+di, j+dj, di, dj), (1000, i, j, -dj, di), (1000, i, j, dj, -di)]
    for neighb_cost, ii, jj, dii, djj in neighbs:
        if (ii, jj) in dead_ends or (ii, jj, dii, djj) in currpath or grid[ii][jj]=="#":
            continue
        currpath.append((ii, jj, dii, djj))
        dfs(ii, jj, dii, djj, targeti, targetj, currcost+neighb_cost, maxcost, currpath, allpaths, dead_ends)
        currpath.pop()
fname = "day16_input.txt"
with open(fname) as file:
    grid = file.read().split()
#print(part1(grid))
part2(grid)
#print(sorted(get_dead_ends(grid)))