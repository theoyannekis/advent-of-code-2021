import csv

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

def isLowPoint(grid, rows, cols, row, col):
    val = grid[(row, col)]
    up = row - 1 < 0 or (row - 1 >= 0 and grid[(row - 1, col)] > val)
    down = row + 1 >= rows or (row + 1 < rows and grid[(row + 1, col)] > val)
    left = col - 1 < 0 or (col - 1 >= 0 and grid[(row, col - 1)] > val)
    right = col + 1 >= cols or (col + 1 < cols and grid[(row, col + 1)] > val)
    return up and down and left and right

def main():
    (grid, rows, cols) = readInput()
    total = 0
    for row in range(rows):
        for col in range(cols):
            if (isLowPoint(grid, rows, cols, row, col)):
                print((row, col))
                total += 1 + grid[(row, col)]
    return total

print(main())