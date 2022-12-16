from functools import cache
from collections import defaultdict, deque

FILE = "input/16.txt"
# FILE = "sample.txt"
f = open(FILE, "r")
lines = f.readlines()

enc = {}
adj = {}
flow = {}
for bit, line in enumerate(lines):
    line = line.strip()
    toks = line.split()
    valve = toks[1]
    rate = int(toks[4][5:-1])
    out = line.split("valve")[-1][1:].lstrip().split(", ")

    enc[valve] = 1 << bit
    adj[valve] = out
    flow[valve] = rate

dist = {}
for st in adj.keys():
    dist[st] = defaultdict(lambda: float('inf'))
    q = deque([(0, st)])
    while q:
        n, u = q.popleft()
        if dist[st][u] > n:
            dist[st][u] = n
            for v in adj[u]:
                q.append((n+1, v))

no_flow = 0
for k, v in flow.items():
    if v == 0:
        no_flow |= enc[k]

P1_mins = 30
P2_mins = 26
start = 'AA'

@cache
def dfs(mins, cur=start, num_guys=0, vis=no_flow):
    if mins == 0: return 0
    ans = 0 if num_guys == 0 else dfs(P2_mins, num_guys=num_guys-1, vis=vis)
    for nxt in adj.keys():
        if flow[nxt] > 0 and (vis & enc[nxt]) == 0:
            if dist[cur][nxt] < mins:
                new_mins = mins - dist[cur][nxt] - 1
                new_vis = vis | enc[nxt]
                ans = max(ans, dfs(new_mins, nxt, num_guys, new_vis) + new_mins * flow[nxt])
    return ans


print(dfs(P1_mins))
print(dfs(P2_mins, num_guys=1))
