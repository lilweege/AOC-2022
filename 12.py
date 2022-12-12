from heapq import heapify, heappush, heappop
FILE = "input/12.txt"
# FILE = "sample.txt"
f = open(FILE, "r")
grid = [[c for c in line.strip()] for line in f.readlines()]
N, M = len(grid), len(grid[0])

starts = []
si = sj = ei = ej = 0
for i in range(N):
    for j in range(M):
        x = grid[i][j]
        if x == 'E':
            grid[i][j] = 'z'
            ei, ej = i, j
        if x == 'S':
            grid[i][j] = 'a'
            si, sj = i, j
        if x == 'a':
            starts.append((i, j))


def dijk(start_coords):
    vis = set()
    pq = [(0, si, sj) for si, sj in start_coords]
    heapify(pq)

    while pq:
        n, ci, cj = heappop(pq)
        if (ci, cj) in vis:
            continue
        vis.add((ci, cj))

        if (ci, cj) == (ei, ej):
            print(n)
            break

        x = ord(grid[ci][cj])
        for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
            if 0 <= ci+di < N and 0 < cj+dj < M:
                if x + 1 >= ord(grid[ci+di][cj+dj]):
                    heappush(pq, (n+1, ci+di, cj+dj))


dijk(start_coords=[(si, sj)])
dijk(start_coords=starts)
