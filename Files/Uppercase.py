handle = open('mbox-short.txt')

for line in handle:
    line = line.rstrip()
    print(line.upper())
