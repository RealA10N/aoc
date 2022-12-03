with open('input', 'r') as text:
    lines = [line.strip() for line in text.readlines()]

def priority(item: str) -> int:
    p = 26 if item.isupper() else 0
    item = item.lower()
    return p + ord(item) - ord('a') + 1

s = 0
for a, b, c in zip(lines[0::3], lines[1::3], lines[2::3]):
    common = set(a).intersection(set(b), set(c))
    assert len(common) == 1
    s += priority(common.pop())
print(s)
