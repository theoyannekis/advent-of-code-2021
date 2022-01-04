import csv

ans = []

def readInput():
    with open('day12.txt', 'r') as fd:
        paths = dict()
        reader = list(csv.reader(fd))
        for row in range(len(reader)):
            spl = reader[row][0].split('-')
            if spl[0] in paths:
                paths[spl[0]].append(spl[1])
            else:
                paths[spl[0]] = [spl[1]]
            if spl[1] in paths:
                paths[spl[1]].append(spl[0])
            else:
                paths[spl[1]] = [spl[0]]
    return paths

def isSmallCave(cave):
    return cave.islower()

def findAllPaths(system, cave, currPath):
    if cave == 'end':
        ans.append(currPath + [cave])
    else:
        for nextCave in system[cave]:
            if (nextCave.isupper() or (nextCave.islower() and nextCave not in currPath)):
                findAllPaths(system, nextCave, currPath + [nextCave])

def main():
    system = readInput()
    findAllPaths(system, 'start', ['start'])
    return len(ans)

print(main())
