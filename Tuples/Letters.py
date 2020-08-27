import string

handle = open('romeo-full.txt')
letterCounter = dict()

for line in handle:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()

    for word in words:
        letterTuple = tuple(word)

        for letter in letterTuple:
            if letter not in letterCounter and letter.isalpha():
                letterCounter[letter] = 1
            elif letter in letterCounter and letter.isalpha():
                letterCounter[letter] += 1

letterList = list()
counterTuple = list(letterCounter.items())

for key, value in counterTuple:
    letterList.append((value, key))

letterList.sort(reverse=True)

for key, value in letterList:
    print(key, value)
