import csv
from functools import reduce

def readInput():
    with open('day10.txt', 'r') as fd:
        lines = []
        reader = list(csv.reader(fd))
        for row in reader:
            s = row[0]
            lines.append(s)
    return lines

def calculateScoreForChar(char):
    if char == '(':
        return 1
    elif char == '[':
        return 2
    elif char == '{':
        return 3
    elif char == '<':
        return 4
    else:
        return 0

def calculateScore(openChars):
    return reduce(lambda x, y: x * 5 + calculateScoreForChar(y), openChars[::-1], 0)

def constructPairings():
    keys = [')', ']', '}', '>']
    vals = ['(', '[', '{', '<']
    return dict(zip(keys, vals))

def findOpenChars(line):
    pairings = constructPairings()
    open = []
    for char in line:
        if char in pairings.values():
            open.append(char)
        elif char in pairings.keys():
            lastOpen = open.pop()
            if lastOpen != pairings[char]:
                return []
    return open


def main():
    lines = readInput()
    openChars = filter(lambda x: len(x) > 0, map(findOpenChars, lines))
    scores = list(map(calculateScore, openChars))
    return sorted(scores)[len(scores) // 2]
print(main())

