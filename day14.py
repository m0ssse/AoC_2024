def part1(robots, t, n, m):
    quad1, quad2, quad3, quad4 = 0, 0, 0, 0
    for x, y, vx, vy in robots:
        x=(x+t*vx)%m
        y=(y+t*vy)%n
        if x<m//2 and y<n//2:
            quad1+=1
        elif x<m//2 and y>n//2:
            quad3+=1
        elif x>m//2 and y<n//2:
            quad2+=1
        elif x>m//2 and y>n//2:
            quad4+=1
    print(quad1*quad2*quad3*quad4)

def draw(robots, n, m):
    grid = [["."]*m for _ in range(n)]
    for j, i in robots:
        grid[i][j]="#"
    for line in grid:
        print(".".join(line))

def count_components(robots):
    res = 0
    visited = set()
    for x, y in robots:
        if (x, y) not in visited:
            res+=1
            visited.add((x, y))
            dfs(x, y, robots, visited)
    return res

def dfs(x, y, robots, visited):
    visited.add((x, y))
    for xx, yy in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        if (xx, yy) in robots and (xx, yy) not in visited:
            visited.add((xx, yy))
            dfs(xx, yy, robots, visited)

def part2(robots, n, m):
    N = n*m
    mincomponents = len(robots)
    for t in range(N):
        robot_positions = set()
        for x, y, vx, vy in robots:
            x=(x+t*vx)%m
            y=(y+t*vy)%n
            robot_positions.add((x, y))
        comps = count_components(robot_positions)
        mincomponents=min(mincomponents, comps)
        if comps==mincomponents:
            print(t)
            draw(robot_positions, n, m)

    print(mincomponents)
fname = "day14_input.txt"
robots = []
with open(fname) as file:
    for line in file:
        xy, vxy = line.strip().split()
        x, y = [int(n) for n in xy.split("=")[-1].split(",")]
        vx, vy = [int(n) for n in vxy.split("=")[-1].split(",")]
        robots.append((x, y, vx, vy))

part1(robots, 100, 103, 101)
part2(robots, 103, 101)