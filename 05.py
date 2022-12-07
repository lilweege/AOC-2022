FILE = "input/05.txt"
# FILE = "sample.txt"
f = open(FILE, "r")
lines = f.readlines()


first_rearrange = lines.index("\n")
N = len(lines[0]) // 4
orig_sts = [[] for _ in range(N)]
for i, line in enumerate(lines[:first_rearrange-1]):
    for st, ch in enumerate(line[1::4]):
        if ch != ' ':
            orig_sts[st].append(ch)

for i in range(N):
    orig_sts[i].reverse()


def solve(is_part1):
    from copy import deepcopy
    sts = deepcopy(orig_sts)
    for line in lines[first_rearrange+1:]:
        x, fr, to = map(int, line.strip().split()[1::2])
        fr, to = fr-1, to-1
        sl = sts[fr][-x:]
        if is_part1: sl.reverse()
        sts[fr] = sts[fr][:-x]
        sts[to].extend(sl)

    print("".join(map(list.pop, sts)))


solve(is_part1=True)
solve(is_part1=False)
