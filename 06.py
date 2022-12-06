FILE = "input/06.txt"
# FILE = "sample.txt"
f = open(FILE, "r")
line = f.readlines()[0]
n = len(line)

def solve(N):
    cnt = [0] * 26
    win = lambda: sum(x == 1 for x in cnt) == N

    for i in range(N):
        cnt[ord(line[i])-ord('a')] += 1
    for i in range(N, n):
        if win(): break
        cnt[ord(line[i-N])-ord('a')] -= 1
        cnt[ord(line[i  ])-ord('a')] += 1
    print(i)

solve(4)
solve(14)
