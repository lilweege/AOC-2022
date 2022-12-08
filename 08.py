FILE = "input/08.txt"
# FILE = "sample.txt"
f = open(FILE, "r")

grid = [list(map(int, line.strip())) for line in f.readlines()]
n = len(grid)


def part1():
    vis = [[False] * n for _ in range(n)]

    for i in range(n):
        big = -1
        for j in range(n):
            if grid[i][j] > big:
                big = grid[i][j]
                vis[i][j] = True

    for i in range(n):
        big = -1
        for j in reversed(range(n)):
            if grid[i][j] > big:
                big = grid[i][j]
                vis[i][j] = True

    for j in range(n):
        big = -1
        for i in range(n):
            if grid[i][j] > big:
                big = grid[i][j]
                vis[i][j] = True

    for j in range(n):
        big = -1
        for i in reversed(range(n)):
            if grid[i][j] > big:
                big = grid[i][j]
                vis[i][j] = True

    cnt = sum(vis[i][j] for j in range(n) for i in range(n))
    print(cnt)


def part2():
    best = 0
    for i in range(n):
        for j in range(n):
            a = b = c = d = 0
            for ni in reversed(range(i)):
                a += 1
                if grid[ni][j] >= grid[i][j]:
                    break

            for ni in range(i+1, n):
                b += 1
                if grid[ni][j] >= grid[i][j]:
                    break

            for nj in reversed(range(j)):
                c += 1
                if grid[i][nj] >= grid[i][j]:
                    break

            for nj in range(j+1, n):
                d += 1
                if grid[i][nj] >= grid[i][j]:
                    break

            score = a * b * c * d
            best = max(best, score)

    print(best)

part1()
part2()
