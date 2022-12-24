FILE = "input/20.txt"
# FILE = "sample.txt"
f = open(FILE, "r")
lines = f.readlines()


# FIXME: This is slow :(
def solve(is_part1):
    lst = list(map(int, lines))
    n = len(lst)

    if not is_part1:
        KEY = 811589153
        lst = [x*KEY for x in lst]

    # (orig_idx) -> curr_idx, value
    curr_inds = list(enumerate(lst))

    for _ in range(1 if is_part1 else 10):
        for i, v in enumerate(lst):

            old_idx = curr_inds[i][0]
            new_idx = (old_idx+v-1) % (n-1) + 1

            if new_idx == old_idx:
                continue
            elif new_idx > old_idx:
                diff = -1
                lo = old_idx + 1
                hi = new_idx
            else:
                diff = 1
                lo = new_idx
                hi = old_idx - 1

            for orig_idx in range(n):
                curr_idx, value = curr_inds[orig_idx]
                if lo <= curr_idx <= hi:
                    curr_inds[orig_idx] = (curr_idx+diff, value)

            curr_inds[i] = (new_idx, curr_inds[i][1])

    a = [val for _, val in sorted(curr_inds, key=lambda t: t[0])]
    z = a.index(0)
    ans = sum(a[(z+o) % len(a)] for o in (1000, 2000, 3000))
    print(ans)


solve(is_part1=True)
solve(is_part1=False)
