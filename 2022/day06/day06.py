def solve(s: str, winsz: int) -> int:
    n = len(s)
    for start, end in zip(range(n), range(winsz, n + 1)):
        win = set(s[start:end])
        if len(win) == winsz:
            return end


with open('input', 'r') as file:
    print(solve(file.read().strip(), int(input('Enter window size: '))))
