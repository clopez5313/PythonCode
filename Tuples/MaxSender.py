handle = open('..\Files\mbox-short.txt')
key = 'From'
length = len(key)
senders = dict()
sndr = None

for line in handle:
    if line.startswith(key) and line[length] != ':':
        line = line.rstrip()
        line = line.split()
        sender = line[1]

        if sender not in senders:
            senders[sender] = 1
        else:
            senders[sender] += 1

tple = list()
tpleList = list(senders.items())

for key, value in tpleList:
    tple.append((value, key))

tple.sort(reverse=True)

for key, value in tple[:1]:
    print(value, key)
