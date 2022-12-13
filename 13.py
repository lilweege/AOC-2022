from functools import cmp_to_key

FILE = "input/13.txt"
# FILE = "sample.txt"
f = open(FILE, "r")
lines = [eval(l) for l in f.readlines() if l != "\n"]
# Eval and isinstance feel like cheating but oh well


def sign(x):
    if x == 0: return 0
    return abs(x) // x

def cmp(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return sign(y - x)
    elif isinstance(x, list) and isinstance(y, list):
        if any(r := cmp(a, b) for a, b in zip(x, y)):
            return r
        return sign(len(y) - len(x))
    elif isinstance(x, int):
        return cmp([x], y)
    else:
        return cmp(x, [y])


def part1():
    print(sum(idx
        for idx, i in enumerate(range(0, len(lines), 2), 1)
            if cmp(lines[i], lines[i+1]) == 1))

def part2():
    d1, d2 = [[2]], [[6]]
    ordered = sorted(lines + [d1, d2], key=cmp_to_key(cmp), reverse=True)
    print((ordered.index(d1) + 1) * (ordered.index(d2) + 1))


part1()
part2()
