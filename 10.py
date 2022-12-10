FILE = "input/10.txt"
# FILE = "sample.txt"
f = open(FILE, "r")
lines = f.readlines()

N = 40
ans1 = 0
ans2 = [[' ' for _ in range(N)] for _ in range(len(lines)*2//N)]

cycle = 1
value = 1
def do_cycle():
    global cycle, ans1, ans2

    if (cycle+20) % N == 0:
        ans1 += cycle * value

    if (cycle-1) % N in (value-1, value, value+1):
        ans2[(cycle-1) // N][(cycle-1) % N] = '#'
    
    cycle += 1


for line in lines:
    if line.startswith('addx'):
        do_cycle()
        do_cycle()
        value += int(line.split()[1])
    else:
        do_cycle()

print(ans1)
print("\n".join("".join(s) for s in ans2))
