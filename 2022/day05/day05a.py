from day05parse import parse

with open('input', 'r') as text:
    buckets, moves = parse(text)

for many, fro, to in moves:
    fro -= 1; to -= 1
    buckets[to].extend(reversed(buckets[fro][-many:]))
    buckets[fro] = buckets[fro][:-many]

print(''.join(b[-1] for b in buckets))
