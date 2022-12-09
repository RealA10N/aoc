from itertools import chain

move_map: dict[str, tuple[int, int]] = {
    'L': (-1, 0),
    'R': (1, 0),
    'U': (0, 1),
    'D': (0, -1),
}


def parse(s: str) -> list[tuple[int, int]]:
    return list(chain.from_iterable(
        (move_map[line.split()[0]],) * int(line.split()[1])
        for line in s.split('\n')
        if line.strip()
    ))


def move_delta(source, delta):
    return tuple(a+b for a, b in zip(source, delta))


def towards(a: int, b: int) -> int:
    # move a one unit towards b
    if a < b:
        return a + 1
    if a > b:
        return a - 1
    return a


def move_tail(head, tail):
    hx, hy = head
    tx, ty = tail
    if abs(hx - tx) < 2 and abs(hy-ty) < 2:
        return tail
    return towards(tx, hx), towards(ty, hy)
