handle = open('..\Files\mbox-short.txt')
key = 'From'
length = len(key)
hours = dict()
hour = None

for line in handle:
    if line.startswith(key) and line[length] != ':':
        line = line.rstrip()
        line = line.split()
        time = line[5]
        tm = time.split(':')
        hour = tm[0]

        if hour not in hours:
            hours[hour] = 1
        else:
            hours[hour] += 1

tple = list()
tpleList = list(hours.items())

for key, value in tpleList:
    tple.append((key, value))

tple.sort()

for key, value in tple:
    print(key, value)
