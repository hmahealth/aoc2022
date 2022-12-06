# X = 1
# Y = 2
# X = 3
# Win = 6, A Y, B Z, C X
# Lose = 0, A Z, B X, C Y
# Tie = 3, A X, B Y, C Z

def calcScore(them, us):
    acc = 0
    if us == "X":
        acc += 1
        if them == "A":
            acc += 3
        elif them == "B":
            acc += 0
        else:
            acc += 6
    elif us == "Y":
        acc += 2
        if them == "A":
            acc += 6
        elif them == "B":
            acc += 3
        else:
            acc += 0
    else:
        acc += 3
        if them == "A":
            acc += 0
        elif them == "B":
            acc += 6
        else:
            acc += 3
    return acc

def convert(them, result):
    if them == "A":
        if result == "X":
            return "Z"
        elif result == "Y":
            return "X"
        else:
            return "Y"
    elif them == "B":
        if result == "X":
            return "X"
        elif result == "Y":
            return "Y"
        else:
            return "Z"
    else:
        if result == "X":
            return "Y"
        elif result == "Y":
            return "Z"
        else:
            return "X"


# we can assign numbers to the letters
# and calculate win or loss based on the
# difference.

f = open("day02.dat", "r")
score = 0
for line in f:
    picks = line.strip().split()
    score = score + calcScore(picks[0], convert(picks[0], picks[1]))

print(score)

