from itertools import pairwise, count
FILE = "input/14.txt"
# FILE = "sample.txt"
f = open(FILE, "r")
lines = f.readlines()


filled_orig = set()
floor = 0
for line in lines:
    pairs = [tuple(map(int, pair.split(","))) for pair in line.split()[::2]]
    floor = max(floor, max(y for _, y in pairs))
    for (px, py), (x, y) in pairwise(pairs):
        if x != px:
            if x < px: x, px = px, x
            for nx in range(px, x+1):
                filled_orig.add((nx, y))
        else:
            if y < py: y, py = py, y
            for ny in range(py, y+1):
                filled_orig.add((x, ny))
floor += 2


# FIXME: This is slow...
# BFS, DFS, or even CA would work for part 2
def solve(is_part1):
    filled = filled_orig.copy()

    if not is_part1:
        for x in range(500-floor, 500+floor+1):
            filled.add((x, floor))

    for step in count():
        x = 500
        for y in range(0, floor+1):
            if (x, y) in filled:
                if (x-1, y) not in filled:
                    x -= 1
                elif (x+1, y) not in filled:
                    x += 1
                else:
                    filled.add((x, y-1))
                    break
        else: break

        if y == 1:
            step += 1
            break

    print(step)


solve(is_part1=True)
solve(is_part1=False)
