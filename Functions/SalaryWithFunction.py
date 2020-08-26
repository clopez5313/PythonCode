def computePay(workedHours,salaryRate):
    rate = salaryRate

    if(workedHours > 40):
        rate = salaryRate * 1.5

    earnedSalary = workedHours * rate

    return earnedSalary

hours = input('Enter hours: ')
rate = input('Enter rate: ')

try:
    hours = int(hours)
    rate = float(rate)
except:
    print('Please enter a numeric value.')
    quit()

salary = computePay(hours,rate)
print(round(salary,2))
