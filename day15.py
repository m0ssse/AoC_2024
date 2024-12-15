def part1(grid, moves):
    #n, m = len(grid), len(grid[0])
    directions = {"<": (0, -1), ">": (0, 1), "v": (1, 0), "^": (-1, 0)}
    boxes = set()
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char =="@":
                roboti, robotj = i, j
            elif char =="O":
                boxes.add((i, j))
    for move in moves:
        topush = False
        di, dj = directions[move]
        nexti, nextj = roboti+di, robotj+dj
        while (nexti, nextj) in boxes:
            topush = True
            nexti+=di
            nextj+=dj
        if grid[nexti][nextj]!="#":
            if topush:
                boxes.remove((roboti+di, robotj+dj))
                boxes.add((nexti, nextj))
            roboti+=di
            robotj+=dj  
    res = 0
    for i, j in boxes:
        res+=100*i+j
    print(res)

fname = "day15_input.txt"
with open(fname) as file:
    grid, moves = file.read().split("\n\n")
moves = moves.replace("\n", "")
grid = grid.split()
part1(grid, moves)
