f = open("day10.dat", "r")
strength = 1
cycles = []

for line in f:
    if line.strip() == "noop":
        cycles.append(strength)
    else:
        inst, val = line.strip().split(" ")
        cycles.append(strength)
        cycles.append(strength)
        strength += int(val)


total = 0
for i in range(20, 220, 40):
    total += i * cycles[i-1]

print(total)


print("-------------------------")


step = 40
lines = []
for i in range(0, 240, step):
    line = ""
    for j in range(0, step):
        sprite = cycles[i+j]
        if (i+j)%step >= sprite-1 and (i+j)%step <= sprite+1:
            line += "X"
        else:
            line += "."
    lines.append(line)

print('\n'.join(lines))
