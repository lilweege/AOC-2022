FILE = "input/07.txt"
# FILE = "sample.txt"
f = open(FILE, "r")
lines = f.readlines()

class Dir:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = {}
        self.sizes = {}

root = Dir("/")
curr = root

n = len(lines)
i = 1  # Skip the first cd, start at root
while i < n:
    line = lines[i].strip()
    i += 1

    if line.startswith('$ cd'):
        newdir = line.split()[-1]
        if newdir == '..':
            curr = curr.parent
        else:
            if newdir in curr.children:
                curr = curr.children[newdir]
            else:
                child = Dir(newdir)
                child.parent = curr
                curr.children[newdir] = child
                curr = child

    elif line.startswith('$ ls'):
        while i < n and not lines[i].startswith('$'):
            size, name = lines[i].split()
            if size != 'dir':
                curr.sizes[name] = int(size)
            i += 1


def dfs(node, cb):
    dir_size = 0
    for sz in node.sizes.values():
        dir_size += sz
    for ch in node.children.values():
        dir_size += dfs(ch, cb)
    cb(dir_size)
    return dir_size


ans1 = 0
MAX_SIZE = 100000
def part1_cb(dir_size):
    global ans1
    if dir_size <= MAX_SIZE:
        ans1 += dir_size


ans2 = float('inf')
TARGET = 70000000 - 30000000
def part2_cb(dir_size):
    global ans2
    if dir_size >= total_size - TARGET:
        ans2 = min(ans2, dir_size)


total_size = dfs(root, part1_cb)
print(ans1)

dfs(root, part2_cb)
print(ans2)
