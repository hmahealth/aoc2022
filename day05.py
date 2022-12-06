file1 = open('day05.dat', 'r')
acc = 0
processing = False
stack = []

for i in range(0,9):
    stack.append([])

def parseStack(line):
    for i in range(0,9):
        item = line[i*4+1]
        if item != " ": stack[i].append(item)

for line in file1:
    if processing:
        if line[0] == "m":
            items = line.split(" ")
            count = int(items[1])
            source = int(items[3])
            dest = int(items[5])
            for i in range(0, count):
                stack[dest-1].insert(0, stack[source-1].pop(0))

    else:
        if line[0] == "[":
            parseStack(line)
        else:
            processing = True
            for i in range(0,9):
                print(stack[i])

for i in range(0,9):
    print(stack[i])



print("------------------------")


file1 = open('day05.dat', 'r')
acc = 0
processing = False
stack = []

for i in range(0,9):
    stack.append([])

def parseStack(line):
    for i in range(0,9):
        item = line[i*4+1]
        if item != " ": stack[i].append(item)

for line in file1:
    if processing:
        if line[0] == "m":
            items = line.split(" ")
            count = int(items[1])
            source = int(items[3])
            dest = int(items[5])
            for i in reversed(range(0, count)):
                stack[dest-1].insert(0, stack[source-1].pop(i))

    else:
        if line[0] == "[":
            parseStack(line)
        else:
            processing = True
            for i in range(0,9):
                print(stack[i])

for i in range(0,9):
    print(stack[i])
