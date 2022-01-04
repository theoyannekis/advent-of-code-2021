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
    return cave.islower() and cave != 'start'

def visitedTwice(visited, nextCave):
    return nextCave in visited and visited[nextCave] >= 2

def findAllPaths(system, cave, currPath, visited):
    if cave == 'end':
        ans.append(currPath + [cave])
    else:
        for nextCave in system[cave]:
            if (nextCave.isupper() or (isSmallCave(nextCave) and not visitedTwice(visited, nextCave))):
                if nextCave in visited:
                    visited[nextCave] += 1
                else:
                    visited[nextCave] = 1
                print(cave, nextCave)
                print(ans)
                findAllPaths(system, nextCave, currPath + [nextCave], visited)
                visited[nextCave] -= 1

def main():
    system = readInput()
    findAllPaths(system, 'start', ['start'], dict())
    return len(ans)

print(main())
