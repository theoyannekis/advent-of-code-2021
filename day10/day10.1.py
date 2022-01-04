import csv

def readInput():
    with open('day10.txt', 'r') as fd:
        lines = []
        reader = list(csv.reader(fd))
        for row in reader:
            s = row[0]
            lines.append(s)
    return lines

def calculateScore(char):
    if char == ')':
        return 3
    elif char == ']':
        return 57
    elif char == '}':
        return 1197
    elif char == '>':
        return 25137
    else:
        return 0

def constructPairings():
    keys = [')', ']', '}', '>']
    vals = ['(', '[', '{', '<']
    return dict(zip(keys, vals))

def firstIllegalChar(line):
    pairings = constructPairings()
    open = []
    for char in line:
        if char in pairings.values():
            open.append(char)
        elif char in pairings.keys():
            lastOpen = open.pop()
            if lastOpen != pairings[char]:
                return char


def main():
    lines = readInput()
    illegalChars = list(map(firstIllegalChar, lines))
    score = sum(map(calculateScore, illegalChars))
    return score
print(main())

