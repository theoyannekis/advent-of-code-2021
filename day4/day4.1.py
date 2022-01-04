import csv

def readNumbers():
    with open('day4Numbers.txt', 'r') as fd:
        reader = csv.reader(fd)
        for row in reader:
            numbers = [int(item) for item in row]
    return numbers

def readBoards():
    with open('day4Boards.txt', 'r') as fd:
        reader = csv.reader(fd)
        boards = []
        for row in reader:
            if len(row) > 0:
                spl = row[0].split(' ')
                filt = list(map(int, filter(lambda x: len(x) > 0, spl)))
                boards.append(filt)

        aggBoards = []
        for i in range(0, len(boards), 5):
            aggBoards.append(boards[i:i+5])
        return aggBoards

def markBoard(board, num):
    rows = len(board)
    cols = len(board[0])
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == num:
                board[row][col] = -num
    return board

def calculateScore(board, num):
    rows = len(board)
    cols = len(board[0])
    score = 0
    for row in range(rows):
        for col in range(cols):
            if board[row][col] > 0:
                score += board[row][col]
    return score * num

def isBoardCompleted(board):
    rows = len(board)
    cols = len(board[0])
    for row in range(rows):
        compCount = 0
        for col in range(cols):
            if board[row][col] < 0:
                compCount += 1
        if compCount == cols:
            return True

    for col in range(cols):
        compCount = 0
        for row in range(rows):
            if board[row][col] < 0:
                compCount += 1
        if compCount == cols:
            return True

    return False


def main():
    input = readNumbers()
    boards = readBoards()
    for num in input:
        for board in boards:
            markBoard(board, num)
            if isBoardCompleted(board):
                return calculateScore(board, num)



print(main())