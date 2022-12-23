from collections import defaultdict

FILE = "input/17.txt"
# FILE = "sample.txt"
f = open(FILE, "r")
flow = list(f.readline().strip())

shapes = [
    [
        0b1111000
    ],
    [
        0b0100000,
        0b1110000,
        0b0100000,
    ],
    [
        0b0010000,
        0b0010000,
        0b1110000,
    ],
    [
        0b1000000,
        0b1000000,
        0b1000000,
        0b1000000,
    ],
    [
        0b1100000,
        0b1100000,
    ],
]

shapes = [x[::-1] for x in shapes]
flow_idx = shape_idx = -1
hist = defaultdict(list)
grid = defaultdict(int)
tops = []
x_pos = []
shape_no = 0
top = 0


def ok(shape, x, y):
    return not (
        x < 0 or  # -x
        y < 0 or  # -y
        any(row & ((1 << x) - 1) for row in shape) or  # +x
        any((row >> x) & grid[y+dy] for dy, row in enumerate(shape))  # +y
    )


while True:
    shape_no += 1
    shape_idx = (shape_idx + 1) % len(shapes)
    shape = shapes[shape_idx]

    x, y = 2, top + 3
    while True:
        flow_idx = (flow_idx + 1) % len(flow)
        arrow = flow[flow_idx]

        dx = 1 if arrow == ">" else -1
        if ok(shape, x+dx, y):
            x += dx

        if not ok(shape, x, y-1):
            break
        y -= 1

    for dy, row in enumerate(shape):
        if grid[y+dy] == 0:
            top += 1
        grid[y+dy] |= row >> x

    tops.append(top)
    x_pos.append(x)
    hist[(shape_idx, flow_idx)].append(shape_no)
    matching_shapes = hist[(shape_idx, flow_idx)]

    done = False
    for idx, last_shape in enumerate(matching_shapes[:-1]):
        for first_shape in reversed(matching_shapes[:idx]):
            if x_pos[first_shape:last_shape] == x_pos[last_shape:]:
                cycle_start = last_shape - 1
                cycle_len = last_shape - first_shape
                cycle_height = top - tops[cycle_start]
                done = True
                break
        if done: break
    if done: break


def solve(num_shapes):
    diff = num_shapes - cycle_start
    repeat = diff // cycle_len
    offset = diff % cycle_len
    return tops[cycle_start + offset - 1] + cycle_height * repeat


print(solve(2022))
print(solve(1000000000000))
