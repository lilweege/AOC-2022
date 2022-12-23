from collections import defaultdict

FILE = "input/23.txt"
# FILE = "sample.txt"
f = open(FILE, "r")
grid = [[x for x in s.strip()] for s in f.readlines()]


def solve(is_part1):
    points = set((i, j)
        for i in range(len(grid))
        for j in range(len(grid[i]))
            if grid[i][j] == '#')

    for round in range(10  if is_part1 else int(1e9)):
        new_elves = defaultdict(list)
        
        for (i, j) in points:
            do_nothing = True
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    if di == 0 and dj == 0:
                        continue
                    if (i+di, j+dj) in points:
                        do_nothing = False
                        break
                else: continue
                break

            if not do_nothing:
                dirs = (
                    ((i-1, j-1), (i-1, j  ), (i-1, j+1)),
                    ((i+1, j-1), (i+1, j  ), (i+1, j+1)),
                    ((i-1, j-1), (i  , j-1), (i+1, j-1)),
                    ((i-1, j+1), (i  , j+1), (i+1, j+1)),
                )
                xx = round % 4
                for check in dirs[xx:] + dirs[:xx]:
                    if not any(map(points.__contains__, check)):
                        new_elves[check[1]].append((i, j))
                        break

        if len(new_elves) == 0:
            print(round + 1)
            return

        for fr, v in list(new_elves.items()):
            if len(v) == 1:
                points.remove(v[0])
                points.add(fr)

    mii = mij = float("inf")
    mai = maj = -float("inf")
    for (i, j) in points:
        mii, mij = min(mii, i), min(mij, j)
        mai, maj = max(mai, i), max(maj, j)

    ans = (maj - mij + 1) * (mai - mii + 1) - len(points)
    print(ans)


solve(is_part1=True)
solve(is_part1=False)
