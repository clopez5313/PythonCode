import re

handle = open('..\Files\mbox-short.txt')
numbers = list()

for line in handle:
    line = line.rstrip()
    number = re.findall('^New Revision: ([0-9]+)', line)

    if len(number) > 0:
        num = int(number[0])
        numbers.append(num)

if len(numbers) > 0:
    print(round(sum(numbers)/len(numbers)))
else:
    print(0.0)
