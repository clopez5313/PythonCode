hours = input('Enter hours: ')
rate = input('Enter rate: ')

try:
    hours = int(hours)
    rate = float(rate)
except:
    print('Please enter a numeric value.')
    quit()

if(hours > 40):
    rate = rate * 1.5

salary = hours * rate
print(round(salary,2))
