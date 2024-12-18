def part1(bytes):
    n, m = 71, 71
    grid = [['.']*m for _ in range(n)]
    for i in range(1024):
        x, y = bytes[i]
        grid[y][x] = "#"
    bfs(grid)

def bfs(grid):
    n, m = len(grid), len(grid[0])
    queue = [(0, 0, 0)]
    visited = set()
    k = 0
    while k<len(queue):
        i, j, steps = queue[k]
        visited.add((i, j))
        if i==n-1 and j==m-1:
            #print(steps)
            return True
        for ii, jj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if ii<0 or ii>=n or jj<0 or jj>=m or (ii, jj) in visited or grid[ii][jj]=="#":
                continue
            queue.append((ii, jj, steps+1))
            visited.add((ii, jj))
        k+=1
    return False

def part2(bytes):
    n, m = 71, 71
    grid = [['.']*m for _ in range(n)]
    i=0
    while bfs(grid):
        x, y = bytes[i]
        grid[y][x]="#"
        i+=1
    print(x, y)


fname = "day18_input.txt"
with open(fname) as file:
    bytes = [[int(x) for x in line.split(",")] for line in file.readlines()]
part1(bytes)
part2(bytes)