def part1(bytes):
    n, m = 71, 71
    grid = [['.']*m for _ in range(n)]
    for i in range(1024):
        x, y = bytes[i]
        grid[y][x] = "#"
    print(bfs(grid))

def bfs(grid):
    n, m = len(grid), len(grid[0])
    queue = [(0, 0, 0)]
    visited = set()
    k = 0
    while k<len(queue):
        i, j, steps = queue[k]
        visited.add((i, j))
        if i==n-1 and j==m-1:
            return steps
        for ii, jj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if ii<0 or ii>=n or jj<0 or jj>=m or (ii, jj) in visited or grid[ii][jj]=="#":
                continue
            queue.append((ii, jj, steps+1))
            visited.add((ii, jj))
        k+=1
    return 0

def part2(bytes):
    n, m = 71, 71
    grid = [['.']*m for _ in range(n)]
    parents = {}
    compsize = {}
    for x, y in bytes:
        grid[y][x]="#"
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char==".":
                parents[(i, j)]=(i, j)
                compsize[(i, j)]=1
                for ii, jj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if ii<0 or ii>=n or jj<0 or jj>=m or grid[ii][jj]=="#":
                        continue
                    if (ii, jj) not in parents:
                        parents[(ii, jj)] = (ii, jj)
                        compsize[(ii, jj)]=1
                    merge(parents, (i, j), (ii, jj), compsize)
    k=-1
    while repres(parents, (0, 0))!=repres(parents, (n-1, m-1)):
        j, i = bytes[k]
        grid[i][j]="."
        parents[(i, j)]=(i, j)
        compsize[(i, j)]=1
        for ii, jj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if ii<0 or ii>=n or jj<0 or jj>=m or grid[ii][jj]=="#":
                continue
            merge(parents, (i, j), (ii, jj), compsize)
        k-=1
    print(j, i)

def merge(parents, a, b, compsize):
    a, b = repres(parents, a), repres(parents, b)
    if a==b:
        return
    if compsize[a]<compsize[b]:
        a, b = b, a
    parents[b]=a
    compsize[a]+=compsize[b]

def repres(parents, x):
    if x not in parents:
        parents[x] = x
    while x!=parents[x]:
        x = parents[x]
    return x


fname = "day18_input.txt"
with open(fname) as file:
    bytes = [[int(x) for x in line.split(",")] for line in file.readlines()]
part1(bytes)
part2(bytes)
