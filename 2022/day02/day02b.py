with open('input', 'r') as text:
    lines = [line.strip() for line in text.readlines()]

toint = {
    'A': 0,
    'B': 1,
    'C': 2,
    'X': 0,
    'Y': 1,
    'Z': 2,
}

# Lets mark with A the opponents move, and with B the result.
# Tie if B=1: Score is A+3
# Win if B=2: Score is (A+1)+6
# Lose if B=0: Score is (A-1)+0

sum = 0
for turn in lines:
    a, b = (toint[move.strip()] for move in turn.split())

    # I use modulo starting from 0,
    # and thus each turn adds an additional point to the sum anyway.
    sum += 1

    match b:
        case 1:
            sum += a+3
        case 2:
            sum += ((a+1)%3) + 6
        case 0:
            sum += (a-1) % 3

print(sum)
