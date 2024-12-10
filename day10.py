def solve(grid):
    res1 = 0
    res2 = 0
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char=="0":
                found = set()
                res2+=dfs(grid, i, j, found)
                res1+=len(found)
    print(res1)
    print(res2)

def dfs(grid, i, j, found):
    if int(grid[i][j])==9:
        found.add((i, j))
        return 1
    res = 0
    n, m = len(grid), len(grid[0])
    for ii, jj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if ii<0 or ii>=n or jj<0 or jj>=m:
            continue
        if int(grid[ii][jj])==int(grid[i][j])+1:
            res+=dfs(grid, ii, jj, found)
    return res

fname = "day10_input.txt"
with open(fname) as myfile:
    grid = myfile.read().split()
solve(grid)
