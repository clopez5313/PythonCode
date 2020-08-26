numList = list()

while True:
    number = input('Please enter a number: ')

    if number=='done':
        break

    try:
        number = int(number)
    except:
        print('Please enter a numeric value.')
        continue

    numList.append(number)

print('Maximum:',max(numList))
print('Minimum:',min(numList))
