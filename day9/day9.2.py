import csv
from functools import reduce

def readInput():
    with open('day9.txt', 'r') as fd:
        reader = list(csv.reader(fd))
        grid = dict()
        rows = len(reader)
        cols = len(reader[0][0])
        for row in range(len(reader)):
            s = reader[row][0]
            for col in range(len(s)):
                grid[(row, col)] = int(s[col])
    return (grid, rows, cols)

def isOutOfIndex(rows, cols, row, col):
    return row < 0 or row >= rows or col < 0 or col >= cols

def dfs(grid, rows, cols, row, col):
    if isOutOfIndex(rows, cols, row, col) or grid[(row, col)] == -1 or grid[(row, col)] == 9:
        return 0
    grid[(row, col)] = -1
    return 1 + dfs(grid, rows, cols, row - 1, col) + dfs(grid, rows, cols, row + 1, col) + dfs(grid, rows, cols, row, col - 1) + dfs(grid, rows, cols, row, col + 1)


    return 2

def main():
    (grid, rows, cols) = readInput()
    basins = []
    for row in range(rows):
        for col in range(cols):
            if grid[(row, col)] != -1 and grid[(row, col)] != 9:
                basins.append(dfs(grid, rows, cols, row, col))
    print(basins)
    print(sorted(basins, reverse=True))
    return reduce(lambda x, y: x * y, sorted(basins, reverse=True)[:3])

print(main())