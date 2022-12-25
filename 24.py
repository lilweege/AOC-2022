from collections import deque

FILE = "input/24.txt"
# FILE = "sample.txt"
f = open(FILE, "r")


grid = [s.strip() for s in f.readlines()]
block_l, new_block_l = set(), set()
block_r, new_block_r = set(), set()
block_u, new_block_u = set(), set()
block_d, new_block_d = set(), set()
for i in range(1, len(grid)-1):
    for j in range(1, len(grid[i])-1):
        if grid[i][j] == '<': block_l.add((i, j))
        elif grid[i][j] == '>': block_r.add((i, j))
        elif grid[i][j] == '^': block_u.add((i, j))
        elif grid[i][j] == 'v': block_d.add((i, j))

start = (0, 1)
end = (len(grid)-1, len(grid[-1])-2)
N, M = len(grid)-2, len(grid[0])-2


b1mod = lambda x, m: (x - 1) % m + 1
in_bounds = lambda i, j: (i, j) == start or (i, j) == end or 1 <= i <= N and 1 <= j <= M
not_blocked = lambda i, j, ss: all((i, j) not in s for s in ss)
ok_before = lambda i, j: in_bounds(i, j) and not_blocked(i, j, (block_l, block_r, block_u, block_d))
ok_after = lambda i, j: in_bounds(i, j) and not_blocked(i, j, (new_block_l, new_block_r, new_block_u, new_block_d))
dep = 0

def bfs(start, end):
    global block_l, new_block_l, block_r, new_block_r, block_u, new_block_u, block_d, new_block_d, dep
    q = [start]
    
    while q:
        new_block_l = {(i, b1mod(j-1, M)) for i, j in block_l}
        new_block_r = {(i, b1mod(j+1, M)) for i, j in block_r}
        new_block_u = {(b1mod(i-1, N), j) for i, j in block_u}
        new_block_d = {(b1mod(i+1, N), j) for i, j in block_d}

        b = set()
        while q:
            r, c = q.pop()
            if (r, c) == end: return
            if not ok_before(r, c): continue
            if ok_after(r+1, c): b.add((r+1, c))
            if ok_after(r-1, c): b.add((r-1, c))
            if ok_after(r, c+1): b.add((r, c+1))
            if ok_after(r, c-1): b.add((r, c-1))
            b.add((r, c))
        q.extend(b)

        block_l = new_block_l
        block_r = new_block_r
        block_u = new_block_u
        block_d = new_block_d
        dep += 1

    assert False, "Unreachable"


bfs(start, end)
print(dep)
bfs(end, start)
bfs(start, end)
print(dep)
