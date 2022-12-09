from day09 import *

with open('input', 'r') as file:
    inp = parse(file.read())

head, tail = (0, 0), (0, 0)
visited = set()
for move in inp:
    head = move_delta(head, move)
    tail = move_tail(head, tail)
    visited.add(tail)

print(len(visited))
