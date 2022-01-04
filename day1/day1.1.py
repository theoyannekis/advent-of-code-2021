import csv
with open('adventDay1.1.rtf', 'r') as fd:
    reader = csv.reader(fd)
    arr = []
    for row in reader:
        row = row[0].replace("\\","")
        arr.append(int(row))
    arr = [104] + arr
    print(arr)
    count = 0
    for i in range(1, len(arr)):
        if (arr[i] > arr[i-1]):
            print(arr[i], arr[i-1])
            count += 1
