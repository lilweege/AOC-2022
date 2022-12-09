from math import dist
FILE = "input/09.txt"
# FILE = "sample.txt"
f = open(FILE, "r")
lines = f.readlines()
dirs = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

def part1():
    vis = set()
    hx = hy = tx = ty = 0
    for line in lines:
        dir, num = line.strip().split()
        num = int(num)
        dx, dy = dirs[dir]

        for _ in range(num):
            px, py = hx, hy
            hx += dx
            hy += dy
            if dist((tx, ty), (hx, hy)) > 1.5:
                tx, ty = px, py
            vis.add((tx, ty))
    print(len(vis))

def solve(N):
    def sign(x): return abs(x) // x
    def move(hx, hy, tx, ty):
        # It's possible to compress this logic, but this is sufficient
        d = dist((hx, hy), (tx, ty))
        dx = hx - tx
        dy = hy - ty
        if d == 2:  # Straight
            if abs(dx) == 2:
                tx += sign(dx)
            else:
                ty += sign(dy)
        elif d > 2:  # Diagonal
            if abs(dx) + abs(dy) > 3:
                tx = hx - sign(dx)
                ty = hy - sign(dy)
            elif abs(dx) == 2:
                tx += sign(dx)
                ty += dy
            else:
                tx += dx
                ty += sign(dy)
        return tx, ty

    vis = set()
    tail = [(0, 0) for _ in range(N)]
    for line in lines:
        dir, num = line.strip().split()
        num = int(num)
        dx, dy = dirs[dir]

        for _ in range(num):
            tail[0] = (tail[0][0]+dx, tail[0][1]+dy)
            for i in range(1, N):
                tail[i] = move(*tail[i-1], *tail[i])
            vis.add(tail[-1])

    print(len(vis))


part1()  # solve(N=2)
solve(N=10)
