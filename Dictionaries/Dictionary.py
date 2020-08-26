handle = open('words.txt')
dictionary = dict()
value = 0

for line in handle:
    words = line.split()

    for word in words:
        dictionary[word] = value
        value = value + 1

print('very' in dictionary)
print('nada' in dictionary)
