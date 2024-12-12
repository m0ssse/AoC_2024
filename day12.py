def solve(grid):
    coords = {}
    visited = set()
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if (i, j) not in visited:
                coords[(i, j)] = set()
                coords[(i, j)].add((i, j))
                visited.add((i, j))
                dfs(i, j, grid, char, coords, i, j, visited)
    res1 = 0
    res2 = 0
    for (i, j), coordset in coords.items():
        res1+=len(coordset)*get_perimeter(grid, coordset)
        res2+=len(coordset)*get_sides(grid, coordset)
    print(res1)
    print(res2)

def dfs(i, j, grid, currchar, coords, starti, startj, visited):
    n, m = len(grid), len(grid[0])
    for ii, jj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if ii<0 or ii>=n or jj<0 or jj>=m or (ii, jj) in visited or grid[ii][jj]!=currchar:
            continue
        visited.add((ii, jj))
        coords[(starti, startj)].add((ii, jj))
        dfs(ii, jj, grid, currchar, coords, starti, startj, visited)

def get_perimeter(grid, coords):
    n, m = len(grid), len(grid[0])
    res = 0
    for i, j in coords:
        for ii, jj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if ii<0 or ii>=n or jj<0 or jj>=m or grid[i][j]!=grid[ii][jj]:
                res+=1
    return res

def get_sides(grid, coords):
    parts_horizontal = {}
    parts_vertical = {}
    n, m = len(grid), len(grid[0])
    for i, j in coords:
        if j==0 or grid[i][j-1]!=grid[i][j]:
            if (j-1, j, j) not in parts_vertical:
                parts_vertical[(j-1, j, j)] = []
            parts_vertical[(j-1, j, j)].append(i)
        if j==m-1 or grid[i][j]!=grid[i][j+1]:
            if (j, j+1, j) not in parts_vertical:
                parts_vertical[(j, j+1, j)] = []
            parts_vertical[(j, j+1, j)].append(i)
        if i==0 or grid[i-1][j]!=grid[i][j]:
            if (i-1, i, i) not in parts_horizontal:
                parts_horizontal[(i-1, i, i)] = []
            parts_horizontal[(i-1, i, i)].append(j)
        if i==n-1 or grid[i][j]!=grid[i+1][j]:
            if (i, i+1, i) not in parts_horizontal:
                parts_horizontal[(i, i+1, i)] = []
            parts_horizontal[(i, i+1, i)].append(j)
    res = 0
    for j_list in parts_vertical.values():
        j_list.sort()
        helper=1
        for k in range(1, len(j_list)):
            if j_list[k]-j_list[k-1]!=1:
                helper+=1
        res+=helper
    for i_list in parts_horizontal.values():
        i_list.sort()
        helper=1
        for k in range(1, len(i_list)):
            if i_list[k]-i_list[k-1]!=1:
                helper+=1
        res+=helper
    return res
    
fname = "day12_input.txt"
with open(fname) as file:
    grid = file.read().split()
solve(grid)
