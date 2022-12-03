with open('input', 'r') as text:
    lines = [line.strip() for line in text.readlines()]

cur = 0
tops = list()

for line in lines:
    if not line:
        tops.append(cur)
        cur = 0
    else:
        cur += int(line)

tops.append(cur)
tops.sort()
print(sum(tops[-3:]))
