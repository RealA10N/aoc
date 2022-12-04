with open('input', 'r') as text:
    lines = [
        tuple(
            tuple(int(x) for x in range.split('-'))
            for range in line.strip().split(',')
        ) for line in text.readlines()
    ]


def contains(a, b):
    return a[0] <= b[0] and b[1] <= a[1]


print(sum(
    contains(a, b) or contains(b, a)
    for a, b in lines
))
