hours = input('Enter hours: ')
rate = input('Enter rate: ')

hours = int(hours)
rate = float(rate)

if(hours > 40):
    rate = rate * 1.5

salary = hours * rate
print(round(salary,2))
