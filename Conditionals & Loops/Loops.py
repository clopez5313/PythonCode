total = 0
count = 0

while True:
    number = input('Please enter a number: ')

    if number=='done':
        break

    try:
        number = int(number)
    except:
        print('Please enter a numeric value.')
        continue

    count = count + 1
    total = total + number

if(count==0):
    print(0,0,0)
else:
    print(total,count,total/count)
