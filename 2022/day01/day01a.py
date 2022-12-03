with open('input', 'r') as text:
    lines = [line.strip() for line in text.readlines()]

curcal, maxcal = 0, 0
for line in lines:
    if not line:
        maxcal = max(curcal, maxcal)
        curcal = 0
    else:
        curcal += int(line)

print(max(curcal, maxcal))
