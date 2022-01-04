import csv

with open('day2.txt', 'r') as fd:
    reader = csv.reader(fd)
    arr = []
    position = 0
    depth = 0
    for row in reader:
        spl = row[0].split(' ')
        dir = spl[0]
        num = int(spl[1])
        if dir == 'forward':
            position += num
        elif dir == 'down':
            depth += num
        else:
            depth -= num

    print(position * depth)

