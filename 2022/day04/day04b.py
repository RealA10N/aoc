with open('input', 'r') as text:
    lines = [
        tuple(
            tuple(int(x) for x in range.split('-'))
            for range in line.strip().split(',')
        ) for line in text.readlines()
    ]


def overlap(a, b):
    return a[0] <= b[0] <= a[1] or a[0] <= b[1] <= a[1]


print(sum(
    overlap(a, b) or overlap(b, a)
    for a, b in lines
))
