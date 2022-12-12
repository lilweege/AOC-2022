from collections import deque
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


def bfs(start_coords):
    vis = set()
    q = deque(start_coords)
    step = 0
    while q:
        d = deque()
        while q:
            ci, cj = q.popleft()
            if (ci, cj) in vis:
                continue
            vis.add((ci, cj))

            if (ci, cj) == (ei, ej):
                print(step)
                return

            x = ord(grid[ci][cj])
            for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
                if 0 <= ci+di < N and 0 < cj+dj < M:
                    if x + 1 >= ord(grid[ci+di][cj+dj]):
                        d.append((ci+di, cj+dj))
        step += 1
        q = d


bfs(start_coords=[(si, sj)])
bfs(start_coords=starts)
