FILE = "input/01.txt"
# FILE = "sample.txt"
f = open(FILE, "r")

x = 0
ans = 0
l = []
for s in f.readlines():
    if s != "\n":
        x += int(s)
    else:
        ans = max(ans, x)
        l.append(x)
        x = 0
l.append(x)

l.sort()
print(l[-1])
print(sum(l[-3:]))
