f = open("day09.dat", "r")

row = 0
col = 1

head = [0,0]
tail = [0,0]
visited = set()
visited.add(tuple(tail))

def follow(head):
    # move tail, log move, return tail
    rowDiff = head[row] - tail[row]
    colDiff = head[col] - tail[col]

    if abs(rowDiff) > 1:
        tail[row] += rowDiff / abs(rowDiff)
        tail[col] = head[col]

    elif abs(colDiff) > 1:
        tail[row] = head[row]
        tail[col] += colDiff / abs(colDiff)

    visited.add(tuple(tail))

def move(direction, steps):
    if direction == "R":
        for d in range(0, steps):
            head[col] = head[col]+1
            follow(head)
    if direction == "L":
        for d in range(0, steps):
            head[col] = head[col]-1
            follow(head)
    if direction == "U":
        for d in range(0, steps):
            head[row] = head[row]+1
            follow(head)
    if direction == "D":
        for d in range(0, steps):
            head[row] = head[row]-1
            follow(head)

for line in f:
    direction, steps = line.strip().split(" ")
    move(direction, int(steps))

print(len(visited))


print("-----------------------")

length = 10
tails = list([0,0] for i in range(0, length))

visited.clear()
visited.add(tuple(tails[0]))

def followalong():
    for i in range(0, length-1):
        rowDiff = tails[i][row] - tails[i+1][row]
        colDiff = tails[i][col] - tails[i+1][col]

        if abs(rowDiff) > 1 and abs(colDiff) > 1:
            tails[i+1][row] += rowDiff / abs(rowDiff)
            tails[i+1][col] += colDiff / abs(colDiff)

        elif abs(rowDiff) > 1:
            tails[i+1][row] += rowDiff / abs(rowDiff)
            tails[i+1][col] = tails[i][col]

        elif abs(colDiff) > 1:
            tails[i+1][row] = tails[i][row]
            tails[i+1][col] += colDiff / abs(colDiff)

    visited.add(tuple(tails[length-1]))

def movehead(direction, steps):
    if direction == "R":
        for d in range(0, steps):
            tails[0][col] = tails[0][col]+1
            followalong()
    if direction == "L":
        for d in range(0, steps):
            tails[0][col] = tails[0][col]-1
            followalong()
    if direction == "U":
        for d in range(0, steps):
            tails[0][row] = tails[0][row]+1
            followalong()
    if direction == "D":
        for d in range(0, steps):
            tails[0][row] = tails[0][row]-1
            followalong()

f.seek(0)
for line in f:
    direction, steps = line.strip().split(" ")
    movehead(direction, int(steps))

print(len(visited))
