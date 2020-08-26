handle = open('mbox-short.txt')
confidence = 0.0
count = 0

for line in handle:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        pos = line.find(' ')
        value = line[pos+1:]
        value = float(value)
        confidence = confidence + value
        count = count + 1

if(count==0):
    print('Average spam confidence:', 0.0)

print('Average spam confidence:', confidence/count)
