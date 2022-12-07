FILE = "input/03.txt"
# FILE = "sample.txt"
f = open(FILE, "r")
lines = f.readlines()


def score(un):
    tot = 0
    for x in un:
        if x.islower():
            tot += ord(x) - ord('a')
        else:
            tot += ord(x) - ord('A') + 26
        tot += 1
    return tot


def part1():
    tot = 0
    for s in map(str.strip, lines):
        h = len(s) // 2
        tot += score(set(s[h:]) & set(s[:h]))

    print(tot)

def part2():
    import string
    N = 3
    tot = 0
    for i in range(0, len(lines), N):
        un = set(string.ascii_letters)
        for s in map(str.strip, lines[i:i+N]):
            un &= set(s)
        tot += score(un)

    print(tot)


part1()
part2()