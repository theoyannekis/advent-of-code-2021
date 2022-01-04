import csv

def windowVal(arr, i):
    return arr[i - 1] + arr[i] + arr[i + 1]

def window(arr, i):
    curr = windowVal(arr, i + 1)
    past = windowVal(arr, i)
    if curr > past:
        return True
    return False

with open('adventDay1.1.rtf', 'r') as fd:
    reader = csv.reader(fd)
    arr = []
    for row in reader:
        row = row[0].replace("\\","")
        arr.append(int(row))
    arr = [104] + arr
    count = 0
    for i in range(1, len(arr)-2):
        if (window(arr, i) == True):
            count += 1
    print(count)