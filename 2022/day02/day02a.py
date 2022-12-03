with open('input', 'r') as text:
    lines = [line.strip() for line in text.readlines()]

toint = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
}

deltas = {
    0: 3,
    1: 6,
    2: 0,
}

# Lets mark with A the opponents move, and with B my move.
# Tie if A=B: Score is B+3
# Win if B-A=1: Score is B+6
# Lose if B-A=-1: Score is B

sum = 0
for turn in lines:
    a, b = (toint[move.strip()] for move in turn.split())
    sum += b + deltas[(b - a) % 3]
print(sum)
