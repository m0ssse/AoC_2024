def part1(fname):
    antennas_per_freq = {}
    with open(fname) as inputfile:
        for i, line in enumerate(inputfile):
            for j, char in enumerate(line.strip()):
                if char!=".":
                    if char not in antennas_per_freq:
                        antennas_per_freq[char]=[]
                    antennas_per_freq[char].append((i, j))
    n, m = i+1, j+1
    res = set()
    for coords in antennas_per_freq.values():
        for i, j in get_antinodes(coords, n, m):
            res.add((i, j))
    print(len(res))

def part2(fname):
    antennas_per_freq = {}
    with open(fname) as inputfile:
        for i, line in enumerate(inputfile):
            for j, char in enumerate(line.strip()):
                if char!=".":
                    if char not in antennas_per_freq:
                        antennas_per_freq[char]=[]
                    antennas_per_freq[char].append((i, j))
    n, m = i+1, j+1
    res = set()
    for coords in antennas_per_freq.values():
        for i, j in get_antinodes2(coords, n, m):
            res.add((i, j))
    print(len(res))


def get_antinodes(coord_list, n, m):
    res = set()
    for i in range(len(coord_list)):
        i1, j1 = coord_list[i]
        for j in range(i):
            i2, j2 = coord_list[j]
            di, dj = i2-i1, j2-j1
            ii1, jj1 = i2+di, j2+dj
            ii2, jj2 = i1-di, j1-dj
            if 0<=ii1<n and 0<=jj1<m:
                res.add((ii1, jj1))
            if 0<=ii2<n and 0<=jj2<m:
                res.add((ii2, jj2))
    return res

def get_antinodes2(coord_list, n, m):
    res = set()
    for i in range(len(coord_list)):
        i1, j1 = coord_list[i]
        for j in range(i):
            i2, j2 = coord_list[j]
            di, dj = i2-i1, j2-j1
            ii1, jj1 = i2+di, j2+dj
            ii2, jj2 = i1-di, j1-dj
            res.add((i1, j1))
            res.add((i2, j2))
            while 0<=ii1<n and 0<=jj1<m:
                res.add((ii1, jj1))
                ii1+=di
                jj1+=dj
            while 0<=ii2<n and 0<=jj2<m:
                res.add((ii2, jj2))
                ii2-=di
                jj2-=dj
    return res
            
part1("day8_input.txt")
part2("day8_input.txt")