import csv

def readInput():
    with open('day6.txt', 'r') as fd:
        reader = csv.reader(fd)
        fish = list(map(int, list(reader)[0]))
        return fish

def simulateFish(d, num, days):
    if (num, days) in d:
        return d[(num, days)]
    if days == 0:
        res = 1
        d[(num, days)] = 1
        return res
    if num == 0:
        res = simulateFish(d, 6, days - 1) + simulateFish(d, 8, days - 1)
        d[(num, days)] = res
        return res
    else:
        res = simulateFish(d, num - 1, days - 1)
        d[(num, days)] = res
        return res

def main():
    fish = readInput()
    d = dict()
    return sum(map(lambda x: simulateFish(d, x, 256), fish))

print(main())