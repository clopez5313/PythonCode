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
        size = len(sender)
        posDomain = sender.find('@')
        sndr = sender[posDomain+1:size]

        if sndr not in senders:
            senders[sndr] = 1
        else:
            senders[sndr] += 1

print(senders)
