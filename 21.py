from collections import defaultdict
from functools import cache

FILE = "input/21.txt"
# FILE = "sample.txt"
f = open(FILE, "r")
lines = f.readlines()


sym = {}
rev_sym = defaultdict(list)
for line in lines:
    monkey, rest = line.strip().split(": ")
    rest = rest.split()
    if len(rest) == 1:
        sym[monkey] = int(rest[0])
    elif len(rest) == 3:
        lhs, op, rhs = rest
        sym[monkey] = (lhs, op, rhs)
        rev_sym[lhs].append((monkey, rest))
        rev_sym[rhs].append((monkey, rest))
    else: assert False


@cache
def evaluate(monkey):
    match sym[monkey]:
        case int(x): return x
        case l, '+', r: return evaluate(l) + evaluate(r)
        case l, '-', r: return evaluate(l) - evaluate(r)
        case l, '*', r: return evaluate(l) * evaluate(r)
        case l, '/', r: return evaluate(l) // evaluate(r)


@cache
def reverse_evaluate(monkey):
    if monkey != "humn" and isinstance(sym[monkey], int):
        return sym[monkey]

    exprs = rev_sym[monkey]
    assert len(exprs) == 1
    (t, (l, op, r)), = exprs

    f = monkey == l
    if t == "root":
        if f: return evaluate(r)
        else: return evaluate(l)

    match op:
        case '+':
            if f: return reverse_evaluate(t) - evaluate(r)
            else: return reverse_evaluate(t) - evaluate(l)
        case '-':
            if f: return reverse_evaluate(t) + evaluate(r)
            else: return evaluate(l) - reverse_evaluate(t)
        case '*':
            if f: return reverse_evaluate(t) // evaluate(r)
            else: return reverse_evaluate(t) // evaluate(l)
        case '/':
            if f: return reverse_evaluate(t) * evaluate(r)
            else: return evaluate(l) // reverse_evaluate(t)
        case x: assert False, x


def part1():
    print(evaluate("root"))


def part2():
    # Simplify part 2 based on this assumption
    assert all(len(v) == 1 for v in rev_sym.values())
    print(reverse_evaluate("humn"))


part1()
part2()
