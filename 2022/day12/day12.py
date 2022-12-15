from typing import Generator

PointType = tuple[int, int]
GridType = dict[PointType, int]
PathMapType = dict[PointType, PointType]


def parse(s: str) -> tuple[PointType, PointType, int, int, GridType]:
    start, end = None, None
    lines = s.splitlines(keepends=False)
    grid = dict()
    rows, cols = len(lines), len(lines[0])
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == 'E':
                c = 'z'
                end = (i,j)
            if c == 'S':
                c = 'a'
                start = (i,j)
            grid[(i,j)] = ord(c) - ord('a')
    return start, end, rows, cols, grid


with open('input', 'r') as file:
    start, end, rows, cols, grid = parse(file.read())


def is_valid(point: PointType) -> bool:
    maxs = rows, cols
    return all(0 <= x < m for x, m in zip(point, maxs))


DELTAS = ((0, 1), (0, -1), (1, 0), (-1, 0))
def neighbors(point: PointType) -> Generator[PointType, None, None]:
    for delta in DELTAS:
        ptag = tuple(d + p for d, p in zip(delta, point))
        if is_valid(ptag):
            yield ptag


def path_length(path: PathMapType, start: PointType, end: PointType) -> int:
    return 0 if start == end else 1+path_length(path, start, path[end])
