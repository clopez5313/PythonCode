handle = open('..\Files\mbox-short.txt')
key = 'From'
length = len(key)
daysCount = dict()

for line in handle:
    if line.startswith(key) and line[length] != ':':
        line = line.rstrip()
        line = line.split()
        day = line[2]

        if day not in daysCount:
            daysCount[day] = 1
        else:
            daysCount[day] += 1

print(daysCount)
