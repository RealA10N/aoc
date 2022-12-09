from day09 import *

with open('input', 'r') as file:
    inp = parse(file.read())


KNOTS = 10
knots = [(0, 0) for _ in range(KNOTS)]
visited = set()

for move in inp:
    knots[0] = move_delta(knots[0], move)
    for i in range(KNOTS-1):
        knots[i+1] = move_tail(knots[i], knots[i+1])
        if i == KNOTS-2:
            visited.add(knots[i+1])

print(len(visited))
