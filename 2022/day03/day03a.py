with open('input', 'r') as text:
    lines = [line.strip() for line in text.readlines()]

def priority(item: str) -> int:
    p = 26 if item.isupper() else 0
    item = item.lower()
    return p + ord(item) - ord('a') + 1

s = 0
for line in lines:
    half = len(line)//2
    both = set(line[:half]).intersection(set(line[half:]))
    s += sum(priority(item) for item in both)
print(s)
