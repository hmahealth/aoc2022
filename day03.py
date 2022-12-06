file1 = open('day03.dat', 'r')
acc = 0

def score(char):
    if char.islower():
        return ord(char) - ord('a') + 1
    else:
        return ord(char) - ord('A') + 27

lines = 0
scores = 0

for line in file1:
    lines += 1

    bag1 = line[:len(line)//2]
    bag2 = line[len(line)//2:]
    #print(bag1 + "\n" + bag2)

    for char in bag1:
        if bag2.find(char) >= 0:
            scores += 1
            acc += score(char)
            break

print(acc)
print(lines)
print(scores)

# Closing files
file1.close()

print("-------------------------")

file1 = open('day03.dat', 'r')
acc = 0
lines = file1.readlines()

for i in range(0, len(lines), 3):
    bag1 = lines[i]
    bag2 = lines[i+1]
    bag3 = lines[i+2]

    for char in bag1:
        if bag2.find(char) >= 0:
            if bag3.find(char) >= 0:
                acc += score(char)
                break

print(acc)
