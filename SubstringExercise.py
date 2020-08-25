str = 'X-DSPAM-Confidence:0.8475'

colon = str.find(':')
number = str[colon+1:]
number = float(number)
print(number)
print(type(number))
