from dataclasses import dataclass
from copy import deepcopy
from math import lcm
FILE = "input/11.txt"
# FILE = "sample.txt"
f = open(FILE, "r")

@dataclass
class Monkey:
    items: list[int]
    op: str
    rhs: int
    mod: int
    true_to: int
    else_to: int
    count: int = 0

big_mod = 1
monkeys_orig = []
chunks = f.read().split("\n\n")
for chunk in chunks:
    lines = chunk.split("\n")
    
    items = list(map(int, lines[1].split(": ")[-1].split(", ")))
    op, rhs = lines[2].split("= old ")[-1].split(" ")
    if rhs == "old":
        assert op == "*"
        rhs = 2
        op = "**"
    else:
        rhs = int(rhs)

    mod = int(lines[3].split(" ")[-1])
    true_to = int(lines[4].split(" ")[-1])
    else_to = int(lines[5].split(" ")[-1])
    monkeys_orig.append(Monkey(items, op, rhs, mod, true_to, else_to))
    big_mod = lcm(big_mod, mod)


def solve(is_part1):
    rounds = 20 if is_part1 else 10000
    monkeys = deepcopy(monkeys_orig)
    for _ in range(rounds):
        for m in monkeys:
            for worry in m.items:
                if m.op == "+": worry += m.rhs
                elif m.op == "*": worry *= m.rhs
                elif m.op == "**": worry **= m.rhs
                else: assert False
                if is_part1:
                    worry //= 3
                worry %= big_mod
                to_idx = m.true_to if worry % m.mod == 0 else m.else_to
                monkeys[to_idx].items.append(worry)
            m.count += len(m.items)
            m.items.clear()

    monkeys.sort(key=lambda m: m.count)
    print(monkeys[-1].count * monkeys[-2].count)


solve(is_part1=True)
solve(is_part1=False)
