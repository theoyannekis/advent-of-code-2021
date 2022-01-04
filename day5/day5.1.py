import csv

def readInput():
    with open('day5.txt', 'r') as fd:
        reader = csv.reader(fd)
        res = []
        for row in reader:
            row = [row[0]] + row[1].split(" -> ") + [row[2]]
            res.append(tuple(map(int, row)))
        return res

def addToDict(d, key):
    if key not in d:
        d[key] = 1
    else:
        d[key] += 1

def buildVertical(d, x, y1, y2):
    for y in range(min(y1, y2), max(y1, y2) + 1):
        key = (x, y)
        addToDict(d, key)

def buildHorizontal(d, y, x1, x2):
    for x in range(min(x1, x2), max(x1, x2) + 1):
        key = (x, y)
        addToDict(d, key)

def buildDiagonal(d, x1, y1, x2, y2):
    length = abs(x2 - x1)
    if x1 < x2:
        xStep = 1
    else:
        xStep = -1
    if y1 < y2:
        yStep = 1
    else:
        yStep = -1
    currLength = 0
    x = x1
    y = y1
    while (abs(x - x1) <= length):
        key = (x, y)
        addToDict(d, key)
        x += xStep
        y += yStep

def buildDict(coords):
    d = dict()
    for (x1, y1, x2, y2) in coords:
        if x1 == x2:
            buildVertical(d, x1, y1, y2)
        elif y1 == y2:
            buildHorizontal(d, y1, x1, x2)
        else:
            buildDiagonal(d, x1, y1, x2, y2)
    return d

def calculateResult(d):
    count = 0
    for (x, y) in d.keys():
        if d[(x, y)] > 1:
            count += 1
    return count

def main():
    coords = readInput()
    d = buildDict(coords)
    res = calculateResult(d)
    return res




print(main())