f = open("day08.dat", "r")
lines = []
count = 0

    
# read the whole file into an array
for line in f:
    row = []
    for c in line.strip():
        row.append(int(c))
    lines.append(row)

def visibleTop(i, j):
    height = lines[i][j]
    for a in range(0, i):
        if lines[a][j] >= height:
            return False
    return True

def visibleBottom(i, j):
    height = lines[i][j]
    for a in range(i+1, len(lines)):
        if lines[a][j] >= height:
            return False
    return True

def visibleLeft(i, j):
    height = lines[i][j]
    for b in range(0, j):
        if lines[i][b] >= height:
            return False
    return True

def visibleRight(i, j):
    height = lines[i][j]
    for b in range(j+1, len(lines[0])):
        if lines[i][b] >= height:
            return False
    return True

def isVisible(i, j):
    if i == 0 or i == len(lines)-1 or j == 0 or j == len(lines[0])-1:
        return True
    return visibleLeft(i, j) or visibleRight(i, j) or visibleTop(i, j) or visibleBottom(i, j)

for i in range(0, len(lines)):
    for j in range(0, len(lines[0])):
        if isVisible(i, j):
            count += 1

print(count)


print("---------------------------------")

biggest = 0

def scenicTop(i, j):
    count = 0
    height = lines[i][j]
    for a in reversed(range(0, i)):
        count += 1
        if lines[a][j] >= height:
            break
    return count

def scenicBottom(i, j):
    count = 0
    height = lines[i][j]
    for a in range(i+1, len(lines)):
        count += 1
        if lines[a][j] >= height:
            break
    return count

def scenicLeft(i, j):
    count = 0
    height = lines[i][j]
    for b in reversed(range(0, j)):
        count += 1
        if lines[i][b] >= height:
            break
    return count

def scenicRight(i, j):
    count = 0
    height = lines[i][j]
    for b in range(j+1, len(lines[0])):
        count += 1
        if lines[i][b] >= height:
            break
    return count

def scenic(i, j):
    if i == 0 or i == len(lines)-1 or j == 0 or j == len(lines[0])-1:
        return 0
    return scenicLeft(i, j) * scenicRight(i, j) * scenicTop(i, j) * scenicBottom(i, j)

for i in range(0, len(lines)):
    for j in range(0, len(lines[0])):
        biggest = max(biggest, scenic(i, j))

print(biggest)
