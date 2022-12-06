f = open("day01a.dat", "r")
i = 0
max = []
acc = 0
for line in f:
    if line.strip() == "":
        max.append(acc)
        acc = 0
    else:
        acc = acc + int(line.strip())

max.sort(reverse=True)
print(max[0] + max[1] + max[2])
