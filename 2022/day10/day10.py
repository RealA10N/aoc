START_X = 1

def parse(s: str) -> list[int]:
    # cycls[i] is X during the cycle i.

    x = START_X
    cycls = [x] * 2
    lines = [
        l.split()
        for l in s.split('\n')
        if l.strip()
    ]

    for cmd, *params in lines:
        cycls.append(x)
        if cmd == 'addx':
            x += int(params[0])
            cycls.append(x)

    return cycls
