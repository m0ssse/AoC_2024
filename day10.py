def part1(grid):
    res = 0
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char=="0":
                found = set()
                dfs(grid, i, j, found)
                res+=len(found)
    print(res)

def part2(grid):
    res = 0
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char=="0":
                found = set()
                currpath = [(i, j)]
                dfs2(grid, i, j, currpath, found)
                res+=len(found)
    print(res)

def dfs(grid, i, j, found):
    if int(grid[i][j])==9:
        found.add((i, j))
        return
    n, m = len(grid), len(grid[0])
    for ii, jj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if ii<0 or ii>=n or jj<0 or jj>=m:
            continue
        if int(grid[ii][jj])==int(grid[i][j])+1:
            dfs(grid, ii, jj, found)

def dfs2(grid, i, j, currpath, allpaths):
    if int(grid[i][j])==9:
        currpath.append((i, j))
        allpaths.add(tuple(currpath))
        return
    n, m = len(grid), len(grid[0])
    for ii, jj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if ii<0 or ii>=n or jj<0 or jj>=m:
            continue
        if int(grid[ii][jj])==int(grid[i][j])+1:
            currpath.append((ii, jj))
            dfs2(grid, ii, jj, currpath, allpaths)
            currpath.pop()

fname = "day10_input.txt"
with open(fname) as myfile:
    grid = myfile.read().split()
part1(grid)
part2(grid)
