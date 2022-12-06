f = open("day06.dat", "r")
pos = 0
stack = []

def unique(stack):
    s = sorted(stack)
    for i in range(0, len(stack)-1):
        if s[i] == s[i+1]:
            return False
    return True

for line in f:
    for char in line:
        if len(stack) < 14:
            stack.append(char)
            pos += 1
        else:
            if unique(stack):
                break
            else:
                stack.pop(0)
                stack.append(char)
                pos += 1

    print(pos)

