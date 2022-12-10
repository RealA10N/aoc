from day10 import parse

with open('input', 'r') as file:
    xs = parse(file.read())


def draw_line(xs):
    print(''.join(
        '@' if x-1 <= cycle <= x+1 else ' '
        for cycle, x in enumerate(xs, start=-1)
    )[1:])


LINES = 6
PER_LINE = 40
for line in range(6):
    start = line * PER_LINE
    end = (line+1) * PER_LINE
    draw_line(xs[start:end+1])
