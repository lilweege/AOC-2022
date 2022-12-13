FILE = "input/13.txt"
# FILE = "sample.txt"
f = open(FILE, "r")


def parse_list(s):
    # return eval(s)  # eval is cheating!
    def parse_impl(s, i):
        assert s[i] == '['
        i += 1
        lst = []
        n = len(s)
        while i < n:
            c = s[i]
            if c == '[':
                j, inner = parse_impl(s, i)
                lst.append(inner)
                i = j
            elif c == ']':
                i += 1
                break
            elif c == ',':
                i += 1
                continue
            else:
                for j in range(i+1, n):
                    if s[j] == ',' or s[j] == ']':
                        break
                lst.append(int(s[i:j]))
                i = j
        return i, lst
    return parse_impl(s, 0)[1]

lists = [parse_list(l.strip()) for l in f.readlines() if l != "\n"]


def cmp(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return (x > y) - (x < y)
    if isinstance(x, int): x = [x]
    if isinstance(y, int): y = [y]
    if any(r := cmp(a, b) for a, b in zip(x, y)):
        return r
    return cmp(len(x), len(y))


def part1():
    print(sum(idx
        for idx, i in enumerate(range(0, len(lists), 2), 1)
            if cmp(lists[i], lists[i+1]) == -1))

def part2():
    d1 = sum(cmp(x, [[2]]) == -1 for x in lists) + 1
    d2 = sum(cmp(x, [[6]]) == -1 for x in lists) + 2
    print(d1 * d2)


part1()
part2()
