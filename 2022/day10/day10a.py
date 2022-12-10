from day10 import parse

with open('input', 'r') as file:
    xs = parse(file.read())

print(sum(
    xs[c] * c
    for c in range(20, 240, 40)
))
