FILE = "input/02.txt"
# FILE = "sample.txt"
f = open(FILE, "r")

m1 = {'A': 'R', 'B': 'P', 'C': 'S'}
m2 = {'X': 'R', 'Y': 'P', 'Z': 'S'}
lose = {'R': 'P', 'P': 'S', 'S': 'R'}
win = {'R': 'S', 'P': 'R', 'S': 'P'}
points = {'R': 1, 'P': 2, 'S': 3}

ans1 = 0
ans2 = 0
for s in f.readlines():
    p1, p2 = s.split()
    p1 = m1[p1]
    p2 = m2[p2]

    x = points[p2]
    if p1 == p2:
        x += 3
    elif (p2 == 'R' and p1 == 'S') or\
            (p2 == 'P' and p1 == 'R') or\
            (p2 == 'S' and p1 == 'P'):
        x += 6
    ans1 += x

    if p2 == 'R': # LOSE
        ans2 += 0 + points[win[p1]]
    elif p2 == 'P': # DRAW
        ans2 += 3 + points[p1]
    else: # WIN
        ans2 += 6 + points[lose[p1]]

print(ans1)
print(ans2)
