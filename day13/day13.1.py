import csv

def readInput():
    with open('day13.txt', 'r') as fd:
        reader = list(csv.reader(fd))
        dots = set()
        folds = []
        index = 0
        dotLines = True
        while index < len(reader):
            line = reader[index]
            if len(line) == 0:
                dotLines = False
                index += 1
                continue
            if dotLines:
                dots.add((int(line[0]), int(line[1])))
            else:
                spl = line[0].split(' ')[2].split('=')
                folds.append((spl[0], int(spl[1])))

            index += 1

    return (dots, folds)

def fold(dots, fold):
    foldCoord = fold[1]
    foldDir = fold[0]
    dotVals = list(dots)
    if foldDir == 'x':
        for (x, y) in dotVals:
            if x > foldCoord:
                newX = foldCoord - (x - foldCoord)
                dots.remove((x, y))
                dots.add((newX, y))
            elif x == foldCoord:
                dots.remove((x, y))
    else:
        for (x, y) in dotVals:
            if y > foldCoord:
                newY = foldCoord - (y - foldCoord)
                dots.remove((x, y))
                dots.add((x, newY))
            elif y == foldCoord:
                dots.remove((x, y))

def main():
    (dots, folds) = readInput()
    for foldIns in folds:
        fold(dots, foldIns)
    return dots
print(main())

