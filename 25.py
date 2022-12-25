FILE = "input/25.txt"
# FILE = "sample.txt"
f = open(FILE, "r")

snafu_to_dec = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
dec_to_snafu = {v:k for k, v in snafu_to_dec.items()}

def decode(s):
    x = 0
    b = 1
    for ch in s[::-1]:
        x += b * snafu_to_dec[ch]
        b *= 5
    return x


def encode(x):
    s = ""
    while x > 0:
        s += dec_to_snafu[(x + 2) % 5 - 2]
        x = round(x / 5)
    return s[::-1]


print(encode(sum(decode(s.strip()) for s in f.readlines())))
