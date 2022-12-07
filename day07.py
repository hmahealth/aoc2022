f = open("day07.dat", "r")
pos = 0
stack = []

class Node:
    def __init__(self, parent, name, size):
        self.parent = parent
        self.name = name
        self.size = size
        self.folders = []
        self.files = []

    def hasFolder(self, name):
        for node in self.folders:
            if node.name == name:
                return True
        return False

    def hasFile(self, name):
        for node in self.files:
            if node.name == name:
                return True
        return False

    def getFolder(self, name):
        for i in range(0, len(self.folders)):
            if self.folders[i].name == name:
                return self.folders[i]
        return current

    def getSize(self):
        # all children
        size = 0
        for node in self.files:
            size += node.size
        for node in self.folders:
            size += node.getSize()
        return size

    def folderSizes(self):
        sizes = []
        sizes.append(self.getSize())
        for node in self.folders:
            sizes.extend(node.folderSizes())
        return sizes


tree = Node(None, "/", 0)
current = tree

def treetop(current):
    while current.parent != None:
        current = current.parent
    return current


for line in f:
    if line[0] == "$":
        if line[2:4] == "cd":
            if line[5:6] == "/":
                current = treetop(current)
            elif line[5:7] == "..":
                current = current.parent
            else:
                if current.hasFolder(line[5:].strip()):
                    current = current.getFolder(line[5:].strip())
                else:
                    # this should probably throw an error
                    print("cd into a non-existing folder")
                
        # elif line[2:4] == "ls":
        #     # we only care about what comes after this
        #     print(line)

    elif line[0:3] == "dir":
        if not current.hasFolder(line[4:].strip()):
            current.folders.append(Node(current, line[4:].strip(), 0))
    else:
        # its a size and filename.
        file = line.strip().split(" ")
        if not current.hasFile(file[1]):
            current.files.append(Node(current, file[1], int(file[0])))


top = treetop(current)
sizes = top.folderSizes()

sum = 0
for size in sizes:
    if size <= 100000:
        sum += size

print(sum)


print("-------------------------")


total = 70000000
required = 30000000
used = top.getSize()
available = total - used
needed = required - available

sizes.sort()
for size in sizes:
    if size >= needed:
        print(size)
        break
