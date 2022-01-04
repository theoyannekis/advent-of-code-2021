import csv

def readInput():
    with open('day6.txt', 'r') as fd:
        reader = csv.reader(fd)
        fish = list(map(int, list(reader)[0]))
        return fish

def simulateFish(num, days):
    if days == 0:
        return 1
    if num == 0:
        return simulateFish(6, days - 1) + simulateFish(8, days - 1)
    else:
        return simulateFish(num - 1, days - 1)

def main():
    fish = readInput()
    return sum(map(lambda x: simulateFish(x, 80), fish))

print(main())