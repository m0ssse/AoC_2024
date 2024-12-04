def part1(grid):
    n, m = len(grid), len(grid[0])
    res = 0
    for i in range(n):
        for j in range(m):
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                res+=get_word(grid, i, j, di, dj, 4)=="XMAS"
    return res

def get_word(grid, i, j, di, dj, L=4):
    n, m = len(grid), len(grid[0])
    currword = ""
    ii, jj = i, j
    for _ in range(L):
        currword+=grid[ii][jj]
        ii+=di
        jj+=dj
        if ii<0 or ii>=n or jj<0 or jj>=m:
            break
    return currword

def part2(grid):
    res = 0
    n, m = len(grid), len(grid[0])
    for i in range(1, n-1):
        for j in range(1, m-1):
            if grid[i][j]=="A":
                if grid[i-1][j-1]=="M" and grid[i-1][j+1]=="M" and grid[i+1][j-1]=="S" and grid[i+1][j+1]=="S":
                    res+=1
                elif grid[i-1][j-1]=="S" and grid[i-1][j+1]=="S" and grid[i+1][j-1]=="M" and grid[i+1][j+1]=="M":
                    res+=1
                elif grid[i-1][j-1]=="S" and grid[i-1][j+1]=="M" and grid[i+1][j-1]=="S" and grid[i+1][j+1]=="M": 
                    res+=1  
                elif grid[i-1][j-1]=="M" and grid[i-1][j+1]=="S" and grid[i+1][j-1]=="M" and grid[i+1][j+1]=="S":
                    res+=1
    return res

with open("day4_input.txt") as myfile:
    contents = [line.strip() for line in myfile]
print(part1(contents))
print(part2(contents))