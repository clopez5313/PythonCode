handle = open('romeo.txt')
wordsList = list()

for line in handle:
    line = line.rstrip()
    words = line.split()

    for word in words:
        try:
            i = wordsList.index(word)
        except:
            wordsList.append(word)
            #print(wordsList)
            continue

wordsList.sort()
print(wordsList)
