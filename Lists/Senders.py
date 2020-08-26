handle = open('..\Files\mbox-short.txt')
count = 0
key = 'From'
length = len(key)

for line in handle:
    if line.startswith(key) and line[length] != ':':
        line = line.rstrip()
        line = line.split()
        print(line[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word.")
