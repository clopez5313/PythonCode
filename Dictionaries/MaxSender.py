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

most = 0

for sender in senders:
    if most==0 or senders[sender] > most:
        most=senders[sender]
        sndr=sender

print(sndr,most)
