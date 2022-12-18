from collections import deque, Counter

FILE = "input/18.txt"
# FILE = "sample.txt"
f = open(FILE, "r")
lines = f.readlines()

dirs = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))

xmi = ymi = zmi = float('inf')
xma = yma = zma = -float('inf')

points = set()
for line in lines:
    line = line.strip()
    x, y, z = map(int, line.split(","))
    xmi, ymi, zmi = min(xmi, x-1), min(ymi, y-1), min(zmi, z-1)
    xma, yma, zma = max(xma, x+1), max(yma, y+1), max(zma, z+1)
    points.add((x, y, z))


def get_sides(s):
    yield from ((x*2+dx, y*2+dy, z*2+dz) for x, y, z in s for dx, dy, dz in dirs)

def part1():
    print(list(Counter(list(get_sides(points))).values()).count(1))


def part2():
    vis = set()
    q = deque([(xmi, ymi, zmi)])
    while q:
        x, y, z = q.popleft()
        if not (xmi <= x <= xma and ymi <= y <= yma and zmi <= z <= zma):
            continue
        if (x, y, z) in vis: continue
        if (x, y, z) in points: continue
        vis.add((x, y, z))
        for dx, dy, dz in dirs:
            q.append((x+dx, y+dy, z+dz))

    print(len(set(get_sides(points)) & set(get_sides(vis))))


part1()
part2()
