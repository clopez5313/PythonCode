import re

handle = open('..\Files\mbox-short.txt')
exp = input('Enter a regular expression: ')
counter = 0

for line in handle:
    line = line.rstrip()

    if re.search(exp, line):
        counter = counter + 1

print('The file had', counter, 'lines that matched', exp)
