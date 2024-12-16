from heapq import heappush, heappop

def part1(grid):
    mincost = 10**15
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char=="S":
                starti, startj = i, j
            if char=="E":
                targeti, targetj = i, j
    visited = {}
    heap = [(0, starti, startj, 0, 1)]

    while heap:
        cost, i, j, di, dj = heappop(heap)
        if (i, j, di, dj) in visited:
            continue
        visited[(i, j, di, dj)] = cost
        if i==targeti and j==targetj:
            mincost = min(cost, mincost)
        neighbs = [(1, i+di, j+dj, di, dj), (1000, i, j, -dj, di), (1000, i, j, dj, -di)]
        for neighb_cost, ii, jj, dii, djj in neighbs:
            if grid[ii][jj]=="#" or (ii, jj, dii, djj) in visited:
                continue
            heappush(heap, (cost+neighb_cost, ii, jj, dii, djj))
    print(mincost)
    return mincost, visited

def part2(grid):
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char=="S":
                starti, startj = i, j
            if char=="E":
                targeti, targetj = i, j
    maxcost, visited = part1(grid)
    allpaths = []
    currpath = set([(starti, startj, 0, 1)])
    dfs(starti, startj, 0, 1, targeti, targetj, 0, maxcost, currpath, allpaths, visited)
    valid_nodes = set()
    for path in allpaths:
        for i, j, _, _ in path:
            valid_nodes.add((i, j))
    print(len(valid_nodes))

def dfs(i, j, di, dj, targeti, targetj, currcost, maxcost, currpath, allpaths, mincosts):
    if currcost>maxcost or currcost>mincosts[(i, j, di, dj)]:
        return
    if i==targeti and j==targetj and currcost==maxcost:
        allpaths.append(list(currpath))
        return
    neighbs = [(1, i+di, j+dj, di, dj), (1000, i, j, -dj, di), (1000, i, j, dj, -di)]
    for neighb_cost, ii, jj, dii, djj in neighbs:
        if (ii, jj, dii, djj) in currpath or grid[ii][jj]=="#":
            continue
        currpath.add((ii, jj, dii, djj))
        dfs(ii, jj, dii, djj, targeti, targetj, currcost+neighb_cost, maxcost, currpath, allpaths, mincosts)
        currpath.remove((ii, jj, dii, djj))
fname = "day16_input.txt"
with open(fname) as file:
    grid = file.read().split()
part2(grid)
