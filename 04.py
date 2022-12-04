FILE = "input/04.txt"
# FILE = "sample.txt"
f = open(FILE, "r")

ans1 = 0
ans2 = 0
for line in f.readlines():
    a, b = line.strip().split(",")
    s1, e1 = map(int, a.split("-"))
    s2, e2 = map(int, b.split("-"))
    if s1 <= s2 <= e2 <= e1 or s2 <= s1 <= e1 <= e2:
        ans1 += 1
    if e2 >= s1 and s2 <= e1:
        ans2 += 1

print(ans1)
print(ans2)
