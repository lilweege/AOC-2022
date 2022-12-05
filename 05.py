FILE = "input/05.txt"
# FILE = "sample.txt"
f = open(FILE, "r")
lines = f.readlines()


N = int(len(lines[0])/4)
orig_sts = [[] for _ in range(N)]
for i, line in enumerate(lines):
    if line.startswith(' 1'):
        continue
    if line == "\n":
        first_rearrange = i
        break
    for st in range(0, len(line)-1, 4):
        orig_sts[int(st/4)].append(line[st+1])

for i in range(N):
    orig_sts[i].reverse()
    try:
        j = orig_sts[i].index(' ')
        orig_sts[i] = orig_sts[i][:j]
    except: pass


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
