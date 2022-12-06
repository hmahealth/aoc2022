file1 = open('day04.dat', 'r')
acc = 0

for line in file1:
    split = line.strip().split(",")
    
    elf1 = split[0]
    elf2 = split[1]

    elf1lo = int(elf1.split("-")[0])
    elf1hi = int(elf1.split("-")[1])
    elf2lo = int(elf2.split("-")[0])
    elf2hi = int(elf2.split("-")[1])

    #if ((elf1lo >= elf2lo and elf1hi <= elf2hi) or (elf2lo >= elf1lo and elf2hi <= elf1hi)):
    #    acc += 1
        
    if elf1lo <= elf2lo and elf2hi <= elf1hi:
        acc += 1

    elif elf2lo <= elf1lo and elf1hi <= elf2hi:
        acc += 1

print(acc)

# Closing files
file1.close()

print("-------------------------")

file1 = open('day04.dat', 'r')
acc = 0

for line in file1:
    split = line.strip().split(",")
    
    elf1 = split[0]
    elf2 = split[1]

    elf1lo = int(elf1.split("-")[0])
    elf1hi = int(elf1.split("-")[1])
    elf2lo = int(elf2.split("-")[0])
    elf2hi = int(elf2.split("-")[1])

    #if ((elf1lo >= elf2lo and elf1hi <= elf2hi) or (elf2lo >= elf1lo and elf2hi <= elf1hi)):
    #    acc += 1
        
    if elf1lo <= elf2lo and elf2lo <= elf1hi:
        acc += 1

    elif elf1lo <= elf2hi and elf2hi <= elf1hi:
        acc += 1

    elif elf2lo <= elf1lo and elf1lo <= elf2hi:
        acc += 1

    elif elf2lo <= elf1hi and elf1hi <= elf2hi:
        acc += 1

print(acc)

# Closing files
file1.close()
