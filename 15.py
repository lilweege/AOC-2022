from dataclasses import dataclass
from re import findall

FILE = "input/15.txt"
# FILE = "sample.txt"
f = open(FILE, "r")
lines = f.readlines()

yy = 2000000
N = 4000000
# yy = 10
# N = 20

@dataclass
class Scanner:
    x: int
    y: int
    manh: int

def manh_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def in_range(x, y, sc):
    return manh_dist(x, y, sc.x, sc.y) <= sc.manh

def one_past(sc):
    yield (sc.x-sc.manh-1, sc.y)
    yield (sc.x+sc.manh+1, sc.y)
    for i, x in enumerate(range(sc.x-sc.manh, sc.x), 1):
        yield (x, sc.y + i)
        yield (x, sc.y - i)
    for i, x in enumerate(reversed(range(sc.x, sc.x+sc.manh+1)), 1):
        yield (x, sc.y + i)
        yield (x, sc.y - i)


scanners = []
intervals = []
for line in lines:
    sx, sy, bx, by = map(int, findall(r'(-?[\d]+)', line))
    manh = manh_dist(sx, sy, bx, by)
    scanners.append(Scanner(sx, sy, manh))

    dst = abs(sy - yy)
    if manh > dst:
        l = sx - (manh - dst)
        r = sx + (manh - dst)
        intervals.append((l, r))

intervals.sort()
ans = 0
s1, e1 = intervals[0]
for s2, e2 in intervals[1:]:
    if s2 > e1:
        ans += e1 - s1
        s1, e1 = s2, e2
    elif e1 < e2:
        e1 = e2
ans += e1 - s1
print(ans)


# FIXME: This is slow...
# Ideas: Spatial partition, gradient descent, binary search, constraint solver
for sc1 in scanners:
    for x, y in one_past(sc1):
        if 0 <= x <= N and 0 <= y <= N:
            if not any(in_range(x, y, sc2) for sc2 in scanners):
                print(x * N + y)
                exit(0)
